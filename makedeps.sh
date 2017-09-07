#!/bin/bash

# REQUIRES:
# cabal-rpm
# mock
# yum (https://bugzilla.redhat.com/show_bug.cgi?id=1474513)

# This script will, hopefully, build a repository containing all the dependencies
# needed for bdcs.

BASEDIR="${PWD}"

# directory for intermediate files
WORKDIR="${PWD}/build"

# directory for the finished repo
REPODIR="${PWD}/repo"

# SRPMs
SRPMDIR="${PWD}/srpms"

### FUNCTIONS
runmock() {
    # We need to use --old-chroot because of https://bugzilla.redhat.com/show_bug.cgi?id=1467299
    mock --configdir "${WORKDIR}/config" -r weldr --old-chroot --resultdir "${WORKDIR}/results" "$@" || exit 1
}


# Convert a hackage package name to a rpm package name
# *usually* this is just "whatever" -> "ghc-whatever", but packages that provide
# executables don't get the ghc prefix, and the tests and rules are hard to reproduce
# here, and the function that does this is only exposed in cabal-rpm via
# writing out a spec file. So just hard code some known exec packages here and
# maybe file a request against cabal-rpm later.
rpmname() {
    local cabalname="$1"

    if [ "$cabalname" = "hsc2hs" ]; then
        echo "$1"
    else
        echo "ghc-$1"
    fi
}

# Build a package in mock
buildpkg() {
    local pkgname="$1"
    local specfile="${pkgname}.spec"
    
    # Download the sources
    spectool --gf "$specfile" -C "${WORKDIR}/sources" || exit 1

    # Start with a fresh results directory
    rm -rf "${WORKDIR}/results"/*

    # Run mock
    runmock --buildsrpm --spec "$specfile" --sources "${WORKDIR}/sources"
    runmock --rebuild "${WORKDIR}/results/${pkgname}-"*.src.rpm

    # Save the results
    mv "${WORKDIR}/results/"*.src.rpm "${SRPMDIR}" || exit 1
    mv "${WORKDIR}/results/"*.rpm "${REPODIR}" || exit 1
    createrepo_c "${REPODIR}" || exit 1

    # dnf unhelpfully caches the metadata from the local repo, so expire the cache
    # each time the local repo is updated
    dnf clean expire-cache
}

# Test whether a package is already available or not
available() {
    local pkgname="$1"

    local result_count="$(dnf repoquery -q --whatprovides "$pkgname" --repofrompath weldr,"$REPODIR" | wc -l)"

    if [ "$result_count" -eq 0 ]; then
        return 1
    else
        return 0
    fi
}

# Find and build the unavailable dependencies for a package
builddeps() {
    local cabalname="$1"
    local pkgname="$(rpmname "${cabalname}")"

    # Loop through the dependencies
    # cabal-rpm fails with weird messages sometimes so try to catch that
    local deplist
    deplist="$(cabal-rpm depends "${cabalname}")"
    if [[ "$?" -ne 0 ]]; then
        exit 1
    fi

    # two exits so that a failure from the while loop subshell actually gets caught
    echo "${deplist}" | grep -v 'in Hackage$' | grep -v '\.pc$' | grep -Fv 'libpthread.so' | while read -r dep ; do
        if [ -z "$dep" ]; then
            continue
        fi
        available "$(rpmname "${dep}")" || rebuild "${dep}" || exit 1
    done || exit 1
}

# Build a package and its dependencies
rebuild() {
    local cabalname="$1"
    local suffix="$2"
    local pkgname="$(rpmname "${cabalname}")"

    # ghc-authenticate-oauth has a requirement on RSA < 2.3, so make
    # sure we don't build too new of a version
    if [ "$cabalname" = "RSA" ]; then
        cabalname="RSA-2.2.0"
    fi

    builddeps "$cabalname"

    # Spit out a spec file and build it
    ( cd "$BASEDIR" &&
      cabal-rpm spec "${cabalname}" &&
      fixspec "${pkgname}" &&
      addsuffix "${pkgname}" "${suffix}" &&
      buildpkg "${pkgname}${suffix}" ) || exit 1
}

# Fix problems in the generated spec files
fixspec() {
    local pkgname="$1"

    # Whether cabal-rpm specifies that tests should be run or not
    # depends on whether it can find the dependencies installed on the
    # host system. Instead of having this dependent behavior (and sometimes
    # having to fix someone else's tests) just always disable tests.
    sed -i 's/%bcond_without tests/%bcond_with tests/' "${pkgname}.spec"

    if [[ "$pkgname" = "ghc-haskell-gi" || "$pkgname" = "ghc-hspec-discover" ]]; then
        # I'm not real clear on what this line intends to do, but it's wrong
        sed -i '/mv %{buildroot}%{_ghcdocdir}\/{,ghc-}%{name}/d' "${pkgname}.spec"
    elif [[ "$pkgname" =~ ^ghc-gi- ]]; then
        # cabal-rpm doesn't think there's a base package, since there's no exposed-modules,
        # so we need to add the %files section and a Requires from -devel
        # This kind of makes the spec file look weird but who cares
        sed -i -e '/^%package devel/a\
Requires: %{name}%{?_isa} = %{version}-%{release}' -e '$a\
\
%files -f %{name}.files\
%license LICENSE' "${pkgname}.spec"
    elif [[ "$pkgname" = "ghc-persistent-sqlite" ]]; then
        # Build persistent-sqlite against the system sqlite library instead of the one it ships with
        sed -i -e '1i\
%global cabal_configure_options -fsystemlib\
BuildRequires: sqlite-devel' "${pkgname}.spec"
    else
        return 0
    fi
}

# If a suffix is requested, append it to the package name
addsuffix() {
    local pkgname="$1"
    local suffix="$2"

    if [ -z "$suffix" ]; then
        return 0
    fi

    mv "${pkgname}.spec" "${pkgname}${suffix}.spec"

    # Add the suffix to the name, and fix the .files names
    # We need to care about the position of the new Provides lines in that
    # you can't use %{version} and %{release} before they are defined.
    # Assume that Source0 is late enough
    sed -i -e 's/^Name:.*/&'"${suffix}/" \
           -e 's/^%files \(.*\)-f %{name}\(.*\)\.files/%files \1-f '"${pkgname}"'\2.files/' \
           -e '/^Source0:/a\
Provides: '"${pkgname}"' = %{version}-%{release}\
Provides: '"${pkgname}"'%{_isa} = %{version}-%{release}' \
           -e '/^%package devel/a\
Provides: '"${pkgname}"'-devel = %{version}-%{release}\
Provides: '"${pkgname}"'-devel%{_isa} = %{version}-%{release}' \
           "${pkgname}${suffix}.spec"
}

# Setup the directories
mkdir -p "${WORKDIR}/config"
mkdir -p "${WORKDIR}/sources"
mkdir -p "${WORKDIR}/results"
mkdir -p "${REPODIR}"
mkdir -p "${SRPMDIR}"
createrepo_c "${REPODIR}"
dnf clean expire-cache

# Create the config file
cp "${PWD}/mock.cfg" "${WORKDIR}/config/weldr.cfg"
echo "
[weldr]
name=weldr
baseurl=file://$REPODIR/
enabled=1
gpgcheck=0
\"\"\"

config_opts['plugin_conf']['bind_mount_opts']['dirs'].append(('$REPODIR', '$REPODIR'))" >> "${WORKDIR}/config/weldr.cfg"


# Before anything, need an up-to-date package list
cabal update

# Build some newer versions of dependencies
# Append -weldr to the package name so they don't conflict with the Fedora versions
if ! available "ghc-memory >= 0.14.6" ; then
    rebuild memory -weldr
fi

if ! available "ghc-gitrev >= 1.3.1" ; then
    rebuild gitrev -weldr
fi

if ! available "ghc-cryptonite >= 0.24" ; then
    rebuild cryptonite -weldr
fi

# Built from a local copy of the .spec
( cd "$BASEDIR" && buildpkg "libgit2" ) || exit 1
( cd "$BASEDIR" && buildpkg "libgit2-glib" ) || exit 1

# Download bdcs and build its deps
( cd build &&
  rm -rf bdcs &&
  git clone https://www.github.com/weldr/bdcs &&
  cd bdcs/importer &&
  builddeps bdcs
) || exit 1

# Same for bdcs-cli
( cd build &&
  rm -rf bdcs-cli &&
  git clone https://www.github.com/weldr/bdcs-cli &&
  cd bdcs-cli &&
  builddeps BDCSCli
) || exit 1

# Don't know how to tell cabal-rpm to include test dependencies, so just
# add one more by hand
if ! available "ghc-hspec"; then
    rebuild hspec
fi

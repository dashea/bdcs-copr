# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name concurrent-extra
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.7.0.11
Release:        1%{?dist}
Summary:        Extra concurrency primitives

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-unbounded-delays-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
%endif
# End cabal-rpm deps

%description
The 'concurrent-extra' package offers among other things the following
selection of synchronisation primitives:

* 'Broadcast': Wake multiple threads by broadcasting a value.

* 'Event': Wake multiple threads by signalling an event.

* 'Lock': Enforce exclusive access to a resource. Also known as a binary
semaphore or mutex. The package additionally provides an alternative that works
in the 'STM' monad.

* 'RLock': A lock which can be acquired multiple times by the same thread.
Also known as a reentrant mutex.

* 'ReadWriteLock': Multiple-reader, single-writer locks. Used to protect shared
resources which may be concurrently read, but only sequentially written.

* 'ReadWriteVar': Concurrent read, sequential write variables.

Please consult the API documentation of the individual modules for more
detailed information.

This package was inspired by the concurrency libraries of Java and Python.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc README.markdown


%changelog
* Fri Sep 29 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.7.0.11-1
- spec file generated by cabal-rpm-0.11.2
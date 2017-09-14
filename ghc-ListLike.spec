# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name ListLike
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        4.5.1
Release:        1%{?dist}
Summary:        Generic support for list-like structures

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-fmlist-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-random-devel
%endif
# End cabal-rpm deps

%description
Generic support for list-like structures in Haskell.

The ListLike module provides a common interface to the various Haskell types
that are list-like. Predefined interfaces include standard Haskell lists,
Arrays, ByteStrings, and lazy ByteStrings. Custom types can easily be made
ListLike instances as well.

ListLike also provides for String-like types, such as String and ByteString,
for types that support input and output, and for types that can handle infinite
lists.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


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
%license COPYRIGHT


%files devel -f %{name}-devel.files
%doc README.md


%changelog
* Thu Sep 14 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 4.5.1-1
- spec file generated by cabal-rpm-0.11.2

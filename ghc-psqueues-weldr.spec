# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name psqueues
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}-weldr
Version:        0.2.3.0
Release:        1%{?dist}
Summary:        Pure priority search queues

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Provides: ghc-psqueues = %{version}-%{release}
Provides: ghc-psqueues%{_isa} = %{version}-%{release}

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif
# End cabal-rpm deps

%description
The psqueues package provides <http://en.wikipedia.org/wiki/Priority_queue
Priority Search Queues> in three different flavors.

* 'OrdPSQ k p v', which uses the 'Ord k' instance to provide fast insertion,
deletion and lookup. This implementation is based on Ralf Hinze's
<http://citeseer.ist.psu.edu/hinze01simple.html A Simple Implementation
Technique for Priority Search Queues>. Hence, it is similar to the
<http://hackage.haskell.org/package/PSQueue PSQueue> library, although it is
considerably faster and provides a slightly different API.

* 'IntPSQ p v' is a far more efficient implementation. It fixes the key type to
'Int' and uses a <http://en.wikipedia.org/wiki/Radix_tree radix tree> (like
'IntMap') with an additional min-heap property.

* 'HashPSQ k p v' is a fairly straightforward extension of 'IntPSQ': it simply
uses the keys' hashes as indices in the 'IntPSQ'. If there are any hash
collisions, it uses an 'OrdPSQ' to resolve those. The performance of this
implementation is comparable to that of 'IntPSQ', but it is more widely
applicable since the keys are not restricted to 'Int', but rather to any
'Hashable' datatype.

Each of the three implementations provides the same API, so they can be used
interchangeably. The benchmarks show how they perform relative to one another,
and also compared to the other Priority Search Queue implementations on
Hackage: <http://hackage.haskell.org/package/PSQueue PSQueue> and
<http://hackage.haskell.org/package/fingertree-psqueue fingertree-psqueue>.

<<http://i.imgur.com/KmbDKR6.png>>

<<http://i.imgur.com/ClT181D.png>>

Typical applications of Priority Search Queues include:

* Caches, and more specifically LRU Caches;

* Schedulers;

* Pathfinding algorithms, such as Dijkstra's and A*.


%package devel
Provides: ghc-psqueues-devel = %{version}-%{release}
Provides: ghc-psqueues-devel%{_isa} = %{version}-%{release}
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


%files -f ghc-psqueues.files
%license LICENSE


%files devel -f ghc-psqueues-devel.files
%doc CHANGELOG


%changelog
* Thu Sep 14 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.3.0-1
- spec file generated by cabal-rpm-0.11.2

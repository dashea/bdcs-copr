# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name free
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        4.12.4
Release:        2%{?dist}
Summary:        Monads for free

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-prelude-extras-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
Free monads are useful for many tree-like structures and domain specific
languages.

If 'f' is a 'Functor' then the free 'Monad' on 'f' is the type of trees whose
nodes are labeled with the constructors of 'f'. The word "free" is used in the
sense of "unrestricted" rather than "zero-cost": 'Free f' makes no constraining
assumptions beyond those given by 'f' and the definition of 'Monad'.
As used here it is a standard term from the mathematical theory of adjoint
functors.

Cofree comonads are dual to free monads. They provide convenient ways to talk
about branching streams and rose-trees, and can be used to annotate syntax
trees. The cofree comonad can be seen as a stream parameterized by a 'Functor'
that controls its branching factor.

More information on free monads, including examples, can be found in the
following blog posts: <http://comonad.com/reader/2008/monads-for-free/>
<http://comonad.com/reader/2011/free-monads-for-less/>.


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


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown doc examples


%changelog
* Tue Sep 12 2017 David Shea <dshea@redhat.com> - 4.12.4-2
- Rebuild against rebuilt dependencies

* Thu Aug  3 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 4.12.4-1
- spec file generated by cabal-rpm-0.11.1
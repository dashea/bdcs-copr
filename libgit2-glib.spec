%if 0%{?rhel} == 7
%global with_python3 0
%else
%global with_python3 1
%endif

%global glib2_version 2.44.0
%global libgit2_version 0.26.0

%global commit0 e8c014fad3e3e8fa24fe1bb708485b0362048280
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           libgit2-glib
Version:        0.26.0
Release:        2%{?dist}.weldr.1
Summary:        Git library for GLib

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Libgit2-glib
Source0:        https://github.com/GNOME/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(libgit2) >= %{libgit2_version}
BuildRequires:  libssh2-devel
%if %{with_python3}
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
%endif
BuildRequires:  vala

# For autogen.sh
BuildRequires:	autoconf-archive
BuildRequires:  gnome-common
BuildRequires:	gtk-doc

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libgit2%{?_isa} >= %{libgit2_version}
%if %{with_python3}
# Depend on python3-gobject for the python3 gi overrides directory.
# If we ever get a libgit2-glib consumer that does not depend on python3,
# it would probably make sense to split it to a separate subpackage.
Requires:       python3-gobject%{?_isa}
%endif

%description
libgit2-glib is a glib wrapper library around the libgit2 git access library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{commit0}
./autogen.sh

%build
%configure \
        --disable-static \
        --disable-silent-rules \
	--enable-gtk-doc \
%if %{with_python3}
        --enable-python
%else
        --disable-python
%endif

%make_build

%install
%make_install
# Remove unwanted la files
rm -vf %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/libgit2-glib-1.0.so.*
%{_libdir}/girepository-1.0/Ggit-1.0.typelib
%if %{with_python3}
%{python3_sitearch}/gi/overrides/*
%endif

%files devel
%{_includedir}/libgit2-glib-1.0/
%{_libdir}/libgit2-glib-1.0.so
%{_libdir}/pkgconfig/libgit2-glib-1.0.pc
%{_datadir}/gir-1.0/Ggit-1.0.gir
%{_datadir}/vala/
%doc %{_datadir}/gtk-doc/

%changelog
* Thu Sep 07 2017 Brian C. Lane <bcl@redhat.com> - 0.26.0-2.weldr.1
- Build with upstream version from github containing the correct gobject annotations

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 0.26.0-1
- Update to 0.26.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.25.0-2
- Rebuild for libgit2 0.26.x

* Thu Feb 16 2017 Kalev Lember <klember@redhat.com> - 0.25.0-1
- Update to 0.25.0

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.25.0-0.1
- Finally backport all patches to build this thing

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.24.4-5
- Backport patches to support libgit-0.25.x

* Tue Jan 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.24.4-4
- Rebuild for libgit2-0.25.x

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.24.4-3
- Rebuild for Python 3.6

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 0.24.4-2
- BR vala instead of obsolete vala-tools subpackage

* Wed Sep 07 2016 Kalev Lember <klember@redhat.com> - 0.24.4-1
- Update to 0.24.4

* Thu Aug 25 2016 Kalev Lember <klember@redhat.com> - 0.24.3-1
- Update to 0.24.3

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 0.24.2-1
- Update to 0.24.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.24.0-2
- Rebuild for libgit2 0.24.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 0.24.0-1
- Update to 0.24.0

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 0.23.10-1
- Update to 0.23.10

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Kalev Lember <klember@redhat.com> - 0.23.8-1
- Update to 0.23.8

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 0.23.6-1
- Update to 0.23.6

* Tue Aug 11 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.23.4-1
- Update to latest upstream version

* Thu Aug  6 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.23.2-1
- Update to latest upstream version

* Tue Aug  4 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.23.0-2
- Pull in post-release fixes from upstream (so micro version bump)

* Thu Jul 30 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 0.23.0-1
- Update to 0.23.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kalev Lember <kalevlember@gmail.com> - 0.22.8-1
- Update to 0.22.8

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 0.22.6-2
- Fix ssh detection

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 0.22.6-1
- Update to 0.22.6

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 0.22.4-1
- Update to 0.22.4
- Use license macro for the COPYING file

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 0.22.2-1
- Update to 0.22.2

* Mon Jan 19 2015 Richard Hughes <rhughes@redhat.com> - 0.22.0-1
- Update to 0.22.0

* Tue Nov 04 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.24-1
- Update to 0.0.24

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.22-1
- Update to 0.0.22

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.20-1
- Update to 0.0.20

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.18-2
- Rebuilt for gobject-introspection 1.41.4

* Mon Jun 30 2014 Ignacio Casal Quinteiro <icq@gnome.org> - 0.0.18-1
- Update to 0.0.18

* Sun Jun 22 2014 Ignacio Casal Quinteiro <icq@gnome.org> - 0.0.16-1
- Update to 0.0.16

* Sun Jun 22 2014 Ignacio Casal Quinteiro <icq@gnome.org> - 0.0.14-1
- Update to 0.0.14

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Mar 25 2014 Ignacio Casal Quinteiro <icq@gnome.org> - 0.0.12-1
- Update to 0.0.12

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 0.0.6-1
- Update to 0.0.6

* Sun Jun 16 2013 Kalev Lember <kalevlember@gmail.com> - 0.0.2-2
- Review fixes: depend on python3-gobject (#974834)

* Sun Jun 16 2013 Kalev Lember <kalevlember@gmail.com> - 0.0.2-1
- Initial Fedora build

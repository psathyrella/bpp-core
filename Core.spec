%define name bpp-seq
%define version 1.7.0
%define release 1
%define _prefix /usr

Summary: The Bio++ SeqLib library.
Name: %{name}
Version: %{version}
Release: %{release}
Vendor: The Bio++ Project
Source: http://kimura.univ-montp2.fr/BioPP/Repositories/sources/%{name}-%{version}.tar.gz
License: CeCILL 2
Group: System Environment/Libraries
BuildRoot: %{_builddir}/%{name}-root
Packager: Julien Dutheil
AutoReq: yes
AutoProv: yes

%description
This library contains utilitary and classes for bio-sequence analysis.
It is part of the Bio++ project.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries for
building applications which use %{name}.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog
%{_prefix}/lib/lib*.so
%{_prefix}/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog
%{_prefix}/lib/lib*.a
%{_prefix}/include/*

%changelog
* Thu Mar 25 2010 Julien Dutheil <julien.dutheil@univ-montp2.fr>
- Version 1.7.0
* Wed Jun 10 2009 Julien Dutheil <jdutheil@birc.au.dk>
- Version 1.6.0
* Thu Dec 11 2008 Julien Dutheil <jdutheil@birc.au.dk>
- Version 1.5.0
* Mon Jul 21 2008 Julien Dutheil <jdutheil@birc.au.dk>
- Version 1.4.1
* Fri Jan 18 2008 Julien Dutheil <Julien.Dutheil@univ-montp2.fr>
- Version 1.4.0
* Fri Jul 06 2007 Julien Dutheil <Julien.Dutheil@univ-montp2.fr>
- Version 1.3.0
* Fri Jan 19 2007 Julien Dutheil <Julien.Dutheil@univ-montp2.fr>
- Version 1.2.0
* Mon Aug 28 2006 Julien Dutheil <Julien.Dutheil@univ-montp2.fr>
- Version 1.1.1
* Tue Apr 18 2006 Julien Dutheil <Julien.Dutheil@univ-montp2.fr>
- Version 1.1.0
* Fri Nov 16 2005 Julien Dutheil <Julien.Dutheil@univ-montp2.fr>
- First draft of the spec file

Summary:	Xynth Window System
Summary(pl):	System okienkowy Xynth Window System
Name:		xynth
Version:	0.7.91
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/xynth/%{name}-%{version}.tar.bz2
# Source0-md5:	6e193a82430528f55c1a9bf178116343
URL:		http://www.xynth.org/
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xynth Window System.

%description -l pl
System okienkowy Xynth Window System.

%package libs
Summary:	Xynth Window System libraries
Summary(pl):	Biblioteki systemu okienkowego Xynth Window System
Group:		Libraries

%description libs
Xynth Window System libraries.

%description libs -l pl
Biblioteki systemu okienkowego Xynth Window System.

%package devel
Summary:	Header files for Xynth Window System libraries
Summary(pl):	Pliki nag³ówkowe bibliotek systemu okienkowego Xynth Window System
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Xynth Window System libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek systemu okienkowego Xynth Window System.

%package static
Summary:	Static Xynth Window System libraries
Summary(pl):	Statyczne biblioteki systemu okienkowego Xynth Window System
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xynth Window System libraries.

%description static -l pl
Statyczne biblioteki systemu okienkowego Xynth Window System.

%prep
%setup -q -n %{name}

%build
%{__make} \
	_INSTALLDIR= \
	INSTALLDIR= \
	_FONTDIR=%{_datadir}/%{name}/fonts/ \
	_CONFDIR=%{_sysconfdir}/%{name}/ \
	_THEMEDIR=%{_datadir}/%{name}/themes/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cp -a dist/{bin,share,include} $RPM_BUILD_ROOT%{_prefix}
cp -a dist/lib $RPM_BUILD_ROOT%{_libdir}
cp -a dist/etc/%{name}/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libwidget.a
%{_libdir}/libxynth.a

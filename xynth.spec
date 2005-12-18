#
Summary:	Xynth Window System
Name:		xynth
Version:	0.7.91
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/xynth/%{name}-%{version}.tar.bz2
# Source0-md5:	6e193a82430528f55c1a9bf178116343
Requires:	%{name}-libs = %{version}-%{release}
URL:		http://www.xynth.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xynth Window System

%package libs
Summary:	Xynth Window System libraries
Group:		Libraries

%description libs
Xynth Window System libraries

%package devel
Summary:	Header files for Xynth Window System libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for ... library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki ....

%package static
Summary:	Static Xynth Window System libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xynth Window System libraries.

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
install -d $RPM_BUILD_ROOT/%{_prefix}
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
cp -a dist/{bin,share,lib,include} $RPM_BUILD_ROOT/%{_prefix}
cp -a dist/etc/%{name}/* $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*
%{_datadir}/%{name}

%files libs
%attr(755,root,root) %{_prefix}/lib/*.so.*
%attr(755,root,root) %{_prefix}/lib/*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_prefix}/lib/libwidget.a
%{_prefix}/lib/libxynth.a

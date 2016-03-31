Summary:	Evolution extension for Exchange MAPI
Summary(pl.UTF-8):	Rozszerzenie Evolution dla Exchange MAPI
Name:		evolution-mapi
Version:	3.20.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Mail
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-mapi/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	8de63ca5aa4fc0f576a5b984996b8a06
URL:		http://projects.gnome.org/evolution/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.9
BuildRequires:	evolution-data-server-devel >= %{version}
BuildRequires:	evolution-devel >= %{version}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	openchange-devel >= 2.3
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	evolution >= %{version}
Requires:	evolution-data-server >= %{version}
Requires:	glib2 >= 1:2.40
Requires:	gtk+3 >= 3.0
Requires:	openchange-libs >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows Evolution to interact with Microsoft Exchange
(2007 and later) and OpenChange servers via MAPI.

%description -l pl.UTF-8
Ten pakiet pozwala programowi Evolution współpracować z serwerami
Microsoft Exchange (w wersji 2007 lub nowszej) lub OpenChange poprzez
MAPI.

%package libs
Summary:	Evolution MAPI library
Summary(pl.UTF-8):	Biblioteka Evolution MAPI
Group:		Libraries
Requires:	evolution-data-server-libs >= %{version}
Requires:	openchange-libs >= 2.3

%description libs
Evolution MAPI library.

%description libs -l pl.UTF-8
Biblioteka Evolution MAPI.

%package devel
Summary:	Development files for Evolution MAPI libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek Evolution MAPI
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	evolution-data-server-devel >= %{version}
Requires:	openchange-devel >= 2.3

%description devel
This package provides development files for Evolution MAPI library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne bibliotek Evolution MAPI.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution-data-server/*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/modules/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendmapi.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendmapi.so
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelmapi.so
%{_libdir}/evolution-data-server/camel-providers/libcamelmapi.urls
%attr(755,root,root) %{_libdir}/evolution-data-server/registry-modules/module-mapi-backend.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-mapi-configuration.so
%{_datadir}/appdata/evolution-mapi.metainfo.xml
%{_datadir}/evolution-data-server/mapi

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexchangemapi-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexchangemapi-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexchangemapi-1.0.so
%{_includedir}/evolution-data-server/mapi
%{_pkgconfigdir}/libexchangemapi-1.0.pc

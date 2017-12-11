Summary:	Evolution extension for Exchange MAPI
Summary(pl.UTF-8):	Rozszerzenie Evolution dla Exchange MAPI
Name:		evolution-mapi
Version:	3.26.3
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Mail
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-mapi/3.26/%{name}-%{version}.tar.xz
# Source0-md5:	bf22942ba46ea43e14480d321886c27f
URL:		http://projects.gnome.org/evolution/
BuildRequires:	cmake >= 3.1
BuildRequires:	evolution-data-server-devel >= %{version}
BuildRequires:	evolution-devel >= %{version}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.46
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	libical-devel
BuildRequires:	openchange-devel >= 2.3
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	evolution >= %{version}
Requires:	evolution-data-server >= %{version}
Requires:	glib2 >= 1:2.46
Requires:	gtk+3 >= 3.10
Requires:	openchange-libs >= 2.3
Obsoletes:	evolution-mapi-libs
Obsoletes:	evolution-mapi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows Evolution to interact with Microsoft Exchange
(2007 and later) and OpenChange servers via MAPI.

%description -l pl.UTF-8
Ten pakiet pozwala programowi Evolution współpracować z serwerami
Microsoft Exchange (w wersji 2007 lub nowszej) lub OpenChange poprzez
MAPI.

%prep
%setup -q

%build
%cmake \
        -DLIBEXEC_INSTALL_DIR=%{_libdir} \
        -DENABLE_SCHEMAS_COMPILE=OFF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%dir %{_libdir}/evolution-mapi
%attr(755,root,root) %{_libdir}/evolution-mapi/libcamelmapi-priv.so
%attr(755,root,root) %{_libdir}/evolution-mapi/libevolution-mapi.so
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendmapi.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendmapi.so
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelmapi.so
%{_libdir}/evolution-data-server/camel-providers/libcamelmapi.urls
%attr(755,root,root) %{_libdir}/evolution-data-server/registry-modules/module-mapi-backend.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-mapi-configuration.so
%{_datadir}/appdata/evolution-mapi.metainfo.xml
%{_datadir}/evolution-data-server/mapi

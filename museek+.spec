Summary:	A Qt soulseek client for Linux
Summary(pl.UTF-8):	Oparty na Qt klient soulseek dla Linuksa
Name:		museek+
Version:	0.2
Release:	9
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://downloads.sourceforge.net/museek-plus/%{name}-%{version}.tar.bz2
# Source0-md5:	66d3eab341e1cd6642f83d329a18c3b5
Patch0:		sitescriptdir.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-python.patch
Patch3:		%{name}-libevent.patch
Patch4:		%{name}-c++.patch
URL:		http://www.museek-plus.org/
BuildRequires:	QtNetwork-devel >= 4
BuildRequires:	QtScript-devel >= 4
BuildRequires:	QtUiTools-devel >= 4
BuildRequires:	cmake >= 2.8.2-2
BuildRequires:	gamin-devel
BuildRequires:	libevent-devel
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libvorbis-devel
BuildRequires:	libxml++2-devel >= 2.6
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	python-PyXML
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel >= 1:2.0
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-linguist >= 4
BuildRequires:	qt4-qmake >= 4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	swig
BuildRequires:	swig-python
BuildRequires:	zlib-devel
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}
Suggests:	%{name}-mucous = %{version}-%{release}
Suggests:	%{name}-murmur = %{version}-%{release}
Suggests:	%{name}-museeq = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++.

This is a meta-package which will install museek daemon and all
available clients.

%description -l pl.UTF-8
Museek+ to aplikacja do współdzielenia plików dla sieci peer-to-peer
Soulseek. Jest napisana w C++.

Ten metapakiet instaluje demona oraz wszystkich dostępnych klientów
museek.

%package core
Summary:	Museek+ core package
Summary(pl.UTF-8):	Podstawowy pakiet Museek+
Group:		Applications/Networking
Requires:	libxml++2 >= 2.6

%description core
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++.

This package contains the museek daemon, setup tools and other
essential files.

%description core -l pl.UTF-8
Museek+ to aplikacja do współdzielenia plików dla sieci peer-to-peer
Soulseek. Jest napisana w C++.

Ten pakiet zawiera demona museek, narzędzia do konfiguracji oraz inne
istotne pliki.

%package bindings
Summary:	Python bindings for Museek+
Summary(pl.UTF-8):	Wiązania Pythona do Museek+
Group:		Applications/Networking
Requires:	%{name}-core = %{version}-%{release}

%description bindings
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++.

This package contains Python bindings for Museek+.

%description bindings -l pl.UTF-8
Museek+ to aplikacja do współdzielenia plików dla sieci peer-to-peer
Soulseek. Jest napisana w C++.

Ten pakiet zawiera wiązania Pythona do Museek+.

%package mucous
Summary:	A Curses Museek+ client
Summary(pl.UTF-8):	Klient Museek+ oparty na Curses
Group:		Applications/Networking
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}

%description mucous
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++.

This package contains a Curses GUI for Museek+.

%description mucous -l pl.UTF-8
Museek+ to aplikacja do współdzielenia plików dla sieci peer-to-peer
Soulseek. Jest napisana w C++.

Ten pakiet zawiera interfejs użytkownika do Museek+ oparty na Curses.

%package murmur
Summary:	A PyGTK Museek+ client
Summary(pl.UTF-8):	Klient Museek+ oparty na PyGTK
Group:		Applications/Networking
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.0

%description murmur
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++.

This package contains a PyGTK GUI for Museek+.

%description murmur -l pl.UTF-8
Museek+ to aplikacja do współdzielenia plików dla sieci peer-to-peer
Soulseek. Jest napisana w C++.

Ten pakiet zawiera graficzny interfejs użytkownika do Museek+ oparty
na PyGTK.

%package museeq
Summary:	A Qt Museek+ client
Summary(pl.UTF-8):	Klient Museek+ oparty na Qt
Group:		Applications/Networking
Requires:	%{name}-core = %{version}-%{release}
# for musetup-qt
Requires:	python-PyQt4

%description museeq
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++.

This package contains a Qt GUI for Museek+.

%description museeq -l pl.UTF-8
Museek+ to aplikacja do współdzielenia plików dla sieci peer-to-peer
Soulseek. Jest napisana w C++.

Ten pakiet zawiera graficzny interfejs użytkownika do Museek+ oparty
na Qt.

%package tools
Summary:	Python tools for Museek+
Summary(pl.UTF-8):	Pythonowe narzędzia dla Museek+
Group:		Applications/Networking
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}

%description tools
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++.

This package contains Python tools for Museek+.

%description tools -l pl.UTF-8
Museek+ to aplikacja do współdzielenia plików dla sieci peer-to-peer
Soulseek. Jest napisana w C++.

Ten pakiet zawiera pythonowe narzędzia dla Museek+.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
grep -r /usr/bin/env . -l | xargs sed -i -e '1s,#!.*env python,#!%{__python},'

%build
mkdir build
cd build
CXXFLAGS="%{rpmcxxflags} -std=c++0x"
%cmake .. \
	-DEVERYTHING=1 \
	-DMANDIR=%{_mandir} \
	-DPYTHON_EXECUTABLE:PATH=%{__python}

%{__make}
#	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files core
%defattr(644,root,root,755)
%doc CREDITS LICENSE README TODO
%attr(755,root,root) %{_bindir}/muscan
%attr(755,root,root) %{_bindir}/muscand
%attr(755,root,root) %{_bindir}/museekd
%attr(755,root,root) %{_bindir}/musetup
%{_mandir}/man1/muscan.1*
%{_mandir}/man1/muscand.1*
%{_mandir}/man1/museekd.1*
%{_mandir}/man1/musetup.1*
%dir %{_datadir}/museek
%{_datadir}/museek/museekd
%{_pixmapsdir}/museek_alt2.png

%files bindings
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_mucipherc.so
%{py_sitedir}/mucipher.py[co]
%{py_sitedir}/mucipherc.py[co]
%dir %{py_sitescriptdir}/museek
%{py_sitescriptdir}/museek/*.py[co]

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mulog
%attr(755,root,root) %{_bindir}/museekchat
%attr(755,root,root) %{_bindir}/museekcontrol
%attr(755,root,root) %{_bindir}/musirc.py
%{_mandir}/man1/mulog.1*
%{_mandir}/man1/museekcontrol.1*

%files mucous
%defattr(644,root,root,755)
%doc mucous/MAINTAINERS
%attr(755,root,root) %{_bindir}/mucous
%dir %{py_sitescriptdir}/pymucous
%{py_sitescriptdir}/pymucous/*.py[co]
%{_mandir}/man1/mucous.1*

%files murmur
%defattr(644,root,root,755)
%doc murmur/{CHANGELOG,MAINTAINERS}
%attr(755,root,root) %{_bindir}/murmur
%attr(755,root,root) %{_bindir}/musetup-gtk
%dir %{py_sitescriptdir}/pymurmur
%{py_sitescriptdir}/pymurmur/*.py[co]
%{_desktopdir}/murmur.desktop
%{_desktopdir}/musetup-gtk.desktop
%{_mandir}/man1/murmur.1*
%{_mandir}/man1/musetup-gtk.1*
%{_pixmapsdir}/murmur-??px.png

%files museeq
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/museeq
%attr(755,root,root) %{_bindir}/musetup-qt
%{_mandir}/man1/museeq.1*
%{_desktopdir}/museeq.desktop
%{_datadir}/museek/museeq
%{_pixmapsdir}/museeq.png

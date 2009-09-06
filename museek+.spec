Summary:	A Qt soulseek client for Linux
Name:		museek+
Version:	0.2
Release:	0.1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/museek-plus/%{name}-%{version}.tar.bz2
# Source0-md5:	66d3eab341e1cd6642f83d329a18c3b5
Patch0:		sitescriptdir.patch
URL:		http://www.museek-plus.org/
BuildRequires:	cmake
BuildRequires:	sed >= 4.0
BuildRequires:	gamin-devel
BuildRequires:	libevent-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml++-devel
BuildRequires:	libxml2-devel
BuildRequires:	python-PyXML
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	qt4-build
BuildRequires:	swig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++. This is a meta-package which will
install museek daemon and all available clients.

%package core
Summary:	Museek+ core package
Group:		Applications/Networking

%description core
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++. This package contains the museek
daemon, setup tools and other essential files.

%package bindings
Summary:	Python bindings for Museek+
Group:		Applications/Networking
Requires:	%{name}-core = %{version}-%{release}

%description bindings
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++. This package contains Python bindings
for Museek+.

%package mucous
Summary:	A Curses Museek+ client
Group:		Applications/Networking
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}

%description mucous
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++. This package contains a Curses GUI for
Museek+.

%package murmur
Summary:	A PyGTK Museek+ client
Group:		Applications/Networking
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	python-pygtk
%if 0%{?fedora} >= 10
BuildArch:	noarch
%endif

%description murmur
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++. This package contains a PyGTK GUI for
Museek+.

%package museeq
Summary:	A Qt Museek+ client
Group:		Applications/Networking
Requires:	%{name}-core = %{version}-%{release}
Requires:	PyQt

%description museeq
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++. This package contains a Qt GUI for
Museek+.

%package tools
Summary:	Python tools for Museek+
Group:		Applications/Networking
Requires:	%{name}-bindings = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
%if 0%{?fedora} >= 10
BuildArch:	noarch
%endif

%description tools
Museek+ is a file-sharing application for the Soulseek peer-to-peer
network. It is written in C++. This package contains Python tools for
Museek+.

%prep
%setup -q
%patch0 -p1
grep -r /usr/bin/env . -l | xargs sed -i -e '1s,#!.*env python,#!%{__python},'

%build
mkdir build
cd build
%cmake \
	-DEVERYTHING=1 \
	-DMANDIR=%{_mandir} \
	..
%{__make} \
	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	-C build \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files core
%defattr(644,root,root,755)
%doc COPYING CREDITS LICENSE README TODO
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
%{py_sitescriptdir}/_mucipherc.so
%{py_sitescriptdir}/mucipher.py*
%{py_sitescriptdir}/mucipherc.py*
%{py_sitescriptdir}/museek

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
%attr(755,root,root) %{_bindir}/mucous
%{py_sitescriptdir}/pymucous
%{_mandir}/man1/mucous.1*

%files murmur
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/murmur
%attr(755,root,root) %{_bindir}/musetup-gtk
%{py_sitescriptdir}/pymurmur
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

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flameshot
Version  : 0.6.0
Release  : 3
URL      : https://github.com/lupoDharkael/flameshot/archive/v0.6.0.tar.gz
Source0  : https://github.com/lupoDharkael/flameshot/archive/v0.6.0.tar.gz
Summary  : Powerful yet simple to use screenshot software
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0
Requires: flameshot-bin = %{version}-%{release}
Requires: flameshot-data = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qttools-dev

%description
Flameshot is a screenshot software, it's
powerful yet simple to use for GNU/Linux

%package bin
Summary: bin components for the flameshot package.
Group: Binaries
Requires: flameshot-data = %{version}-%{release}

%description bin
bin components for the flameshot package.


%package data
Summary: data components for the flameshot package.
Group: Data

%description data
data components for the flameshot package.


%prep
%setup -q -n flameshot-0.6.0
cd %{_builddir}/flameshot-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto  CONFIG+=packaging \
CONFIG-=debug \
CONFIG+=release
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1586856649
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flameshot

%files data
%defattr(-,root,root,-)
/usr/share/applications/flameshot.desktop
/usr/share/bash-completion/completions/flameshot
/usr/share/dbus-1/interfaces/org.dharkael.Flameshot.xml
/usr/share/dbus-1/services/org.dharkael.Flameshot.service
/usr/share/flameshot/translations/Internationalization_ca.qm
/usr/share/flameshot/translations/Internationalization_es.qm
/usr/share/flameshot/translations/Internationalization_fr.qm
/usr/share/flameshot/translations/Internationalization_ka.qm
/usr/share/flameshot/translations/Internationalization_pl.qm
/usr/share/flameshot/translations/Internationalization_ru.qm
/usr/share/flameshot/translations/Internationalization_tr.qm
/usr/share/flameshot/translations/Internationalization_zh_CN.qm
/usr/share/flameshot/translations/Internationalization_zh_TW.qm
/usr/share/icons/hicolor/128x128/apps/flameshot.png
/usr/share/icons/hicolor/48x48/apps/flameshot.png
/usr/share/icons/hicolor/scalable/apps/flameshot.svg
/usr/share/metainfo/flameshot.appdata.xml

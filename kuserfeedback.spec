Name:		kuserfeedback
Version:	1.2.0
Release:	3
Summary:	Framework for collecting user feedback for applications via telemetry and surveys
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		https://kde.org/products/frameworks/
Source0:	https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Charts)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	qt5-assistant
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	qdoc5
BuildRequires:	php-cli
# We get the translations from the qt6 version so the packages can coexist
Suggests:	kuserfeedback-translations

%description
Framework for collecting user feedback for applications via telemetry
and surveys.

%files
%{_kde5_datadir}/qlogging-categories5/org_kde_UserFeedback.categories
%{_kde5_bindir}/userfeedbackctl
%{_kde5_qmldir}/org/kde/userfeedback

%package console
Summary:	Application for viewing feedback collected by kuserfeedback
Group:		Development/KDE and Qt

%description console
Application for viewing feedback collected by kuserfeedback.

%files console
%{_kde5_bindir}/UserFeedbackConsole
%{_kde5_applicationsdir}/org.kde.kuserfeedback-console.desktop
%{_kde5_datadir}/metainfo/org.kde.kuserfeedback-console.appdata.xml
%optional %dir %{_datadir}/KDE/UserFeedbackConsole
%optional %{_datadir}/KDE/UserFeedbackConsole/*.qhc
%optional %{_datadir}/KDE/UserFeedbackConsole/*.qch

#---------------------------------------------

%define kuserfeedbackcore_major 1
%define libkuserfeedbackcore %mklibname KUserFeedbackCore %{kuserfeedbackcore_major}

%package -n %{libkuserfeedbackcore}
Summary:	KUser Feedback Core library
Group:		System/Libraries

%description -n %{libkuserfeedbackcore}
KUser Feedback Core library.

%files -n %{libkuserfeedbackcore}
%{_kde5_libdir}/libKUserFeedbackCore.so.%{kuserfeedbackcore_major}{,.*}

#---------------------------------------------

%define kuserfeedbackwidgets_major 1
%define libkuserfeedbackwidgets %mklibname KUserFeedbackWidgets %{kuserfeedbackwidgets_major}

%package -n %{libkuserfeedbackwidgets}
Summary:	KUser Feedback Widgets library
Group:		System/Libraries

%description -n %{libkuserfeedbackwidgets}
KUser Feedback Widgets library.

%files -n %{libkuserfeedbackwidgets}
%{_kde5_libdir}/libKUserFeedbackWidgets.so.%{kuserfeedbackwidgets_major}{,.*}

#---------------------------------------------

%define develname %mklibname %{name} -d

%package -n %{develname}
Summary:	Development package for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} >= %{EVRD}
Requires:	%{libkuserfeedbackcore} >= %{EVRD}
Requires:	%{libkuserfeedbackwidgets} >= %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Header files for development with %{name}.

%files -n %{develname}
%{_includedir}/KUserFeedback/
%{_kde5_libdir}/libKUserFeedbackCore.so
%{_kde5_libdir}/libKUserFeedbackWidgets.so
%{_kde5_libdir}/cmake/KUserFeedback/
%{_kde5_mkspecsdir}/qt_KUserFeedbackCore.pri
%{_kde5_mkspecsdir}/qt_KUserFeedbackWidgets.pri

#---------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 \
	-DQT_INSTALL_DOCS=%{_docdir}/qt5

%build
%ninja_build -C build

%install
%ninja_install -C build
# We get the translations from the qt6 version so the packages can coexist
rm -rf %{buildroot}%{_datadir}/locale

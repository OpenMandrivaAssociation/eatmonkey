%define url_ver %(echo %{version} | cut -c 1-3)

Name:		eatmonkey
Version:	0.1.4
Release:	2
Summary:	Download manager for Xfce
Group:		Graphical desktop/Xfce
License:	GPLv3
URL:		http://goodies.xfce.org/projects/applications/eatmonkey
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2 
BuildRequires:	ruby-gnome2-devel
BuildRequires:	intltool
BuildArch:	noarch

%description
Eatmonkey is a download manager that works exclusively with aria2, the ultra
fast download utility. It has support for HTTP(s)/FTP, BitTorrent and Metalink
files.

%prep
%setup -q

%build
%configure2_5x

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/eatmonkey
%{_datadir}/applications/eatmonkey.desktop
%{_datadir}/eatmonkey
%{_iconsdir}/hicolor/*/apps/eatmonkey.*
%{_datadir}/pixmaps/eatmonkey-logo.png


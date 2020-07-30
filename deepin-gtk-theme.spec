Name:           deepin-gtk-theme
Version:        17.10.11
Release:        2
Summary:        Deepin GTK Theme
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-gtk-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{summary}.

%prep
%setup -q

%build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_datadir}/themes/deepin/
%{_datadir}/themes/deepin-dark/

%changelog
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 17.10.11-2
- Package init

Summary: NethServer configuration for remi-phpscl
Name: nethserver-remi-phpscl
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools

AutoReq: no



%description
NethServer configuration for remi-phpscl

%prep
%setup

%post

%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

%changelog

* Fri Apr 24 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-1-ns6
- Initial release

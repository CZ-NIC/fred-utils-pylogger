%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%define debug_package %{nil}

Summary: Library contains wrapper for FRED Logger
Name: fred-pylogger
Version: %{our_version}
Release: %{?our_release}%{!?our_release:1}%{?dist}
Source0: %{name}-%{version}.tar.gz
License: GPLv3+
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: CZ.NIC <fred@nic.cz>
Url: https://fred.nic.cz/
BuildRequires: python-setuptools
Requires: python

%description
Python libraries to access logging component of FRED registry system

%prep
%setup -n %{name}-%{version}

%install
python2 setup.py install -cO2 --force --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES --prefix=/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

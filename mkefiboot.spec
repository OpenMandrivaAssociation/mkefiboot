# NOTE: This package is fully arched due to dependency sensitivity.
# Please do not remove archfulness on Requires/Provides.

%define debug_package %{nil}

Name:		mkefiboot
Version:	31.8.0.1
Release:	7
Summary:	Standalone mkefiboot implementation for when Lorax is unavailable
Group:		System/Kernel and hardware
License:	GPLv2+
URL:		https://pagure.io/%{name}
Source0:	https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	efi-srpm-macros
# No signed shim binaries yet...
#Requires:	shim-signed
Requires:	grub2-efi
Requires:	parted
Requires:	dmsetup
Requires:	dosfstools
#Requires:	hfsplus-tools
Requires:	efi-filesystem

# These are the only arches OpenMandriva provides grub2-efi...
ExclusiveArch:  %{efi}

%description
This is a friendly fork of mkefiboot, which is normally part of Lorax.

It builds EFI boot media where the full Lorax package is not available.
Lorax requires Anaconda, the Fedora installer.


%prep
%autosetup -p1
sed -i 's/from distutils.core import setup/from setuptools import setup/' setup.py

%build
%py3_build

%install
%py3_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/py%{name}/
%{python3_sitelib}/%{name}-*

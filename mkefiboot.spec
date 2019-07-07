# NOTE: This package is fully arched due to dependency sensitivity.
# Please do not remove archfulness on Requires/Provides.

%define debug_package %{nil}

Name:           mkefiboot
Version:        31.8.0.1
Release:        1
Summary:        Standalone mkefiboot implementation for when Lorax is unavailable
Group:          System/Kernel and hardware
License:        GPLv2+
URL:            https://pagure.io/%{name}
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

# No signed shim binaries yet...
#Requires:       shim-signed
Requires:       grub2-efi
Requires:       parted
Requires:       dmsetup
Requires:       dosfstools
Requires:       hfsplus-tools

# These are the only arches OpenMandriva provides grub2-efi...
ExclusiveArch:  %{efi}

%description
This is a "friendly fork" standalone copy of mkefiboot that is normally part of Lorax.

This project was made for the express purpose of supporting producing EFI boot capable
media on Linux distributions where the full Lorax software package (which requires
Anaconda, the Red Hat/Fedora installer) would not be available.


%prep
%autosetup -p1


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



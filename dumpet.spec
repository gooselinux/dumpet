Name:           dumpet
Version:        1.1
Release:        1.1%{?dist}
Summary:        A tool to dump and debug bootable CD images
License:        GPLv2+
Group:          Development/Tools
URL:            https://fedorahosted.org/dumpet/
Source0:        https://fedorahosted.org/releases/d/u/dumpet/dumpet-%{version}.tar.bz2
BuildRequires:	popt-devel

%description
DumpET is a utility to aid in the debugging of bootable CD-ROM images.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README TODO COPYING
%{_bindir}/dumpet

%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 1.1-1.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Mon Oct 05 2009 Peter Jones <pjones@redhat.com> - 1.1-1
- Update to dumpet-1.1, which treats CFLAGS reasonably.

* Mon Oct 05 2009 Peter Jones <pjones@redhat.com> - 1.0-1
- First release.


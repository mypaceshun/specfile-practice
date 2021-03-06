Name:		sample-script
Version:	1.0
Release:	2%{?dist}
Summary:	sample script
License:	MIT

Source0:        sample-script-1.0.tar.gz

Patch0:         sample-patch01.patch
Patch1:         sample-patch02.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
sample
script


%prep
echo =====prep=====
rm -rf %{buildroot}
%setup
%patch0 -p1
%patch1 -p1

%build
echo =====build=====
make

%install
echo =====install=====
make install DESTDIR=%{buildroot} BINDIR=%{_bindir} CONFDIR=%{_sysconfdir}

%check
echo =====check=====
make check DESTDIR=%{buildroot} BINDIR=%{_bindir} CONDFIR=%{_sysconfdir}

%clean
echo =====clean=====
make clean

%post
echo =====post=====

%pre
echo =====pre=====

%preun
echo =====preun=====

%postun
echo =====postun=====

%triggerin -- tree
echo =====triggerin=====

%triggerun -- tree
echo =====triggerun=====

%triggerpostun -- tree
echo =====triggerpostun=====

%verifyscript
echo =====verifyscript=====

%files
%attr(0755,root,root) %{_bindir}/sample
%config(noreplace) %{_sysconfdir}/sample/sample.conf
%doc README.md

%changelog
* Thu Dec 06 2018 KAWAI Shun <shun at osstech.co.jp> - 1.0-2
- add new settings

* Thu Dec 06 2018 KAWAI Shun <shun at osstech.co.jp> - 1.0-1
- first release

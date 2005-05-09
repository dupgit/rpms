# $Id$
# Authority: matthias

%define prever RC1
%define xmms_inputdir %(xmms-config --input-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/Input)

Summary: X MultiMedia System input plugin to play mpegplus (mpc) files
Name: xmms-musepack
Version: 1.2
Release: 0.1%{?prever:.%{prever}}
License: BSD
Group: Applications/Multimedia
URL: http://www.musepack.net/
Source: http://musepack.origean.net/files/linux/plugins/xmms-musepack-%{version}%{?prever:-%{prever}}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: xmms-devel, libmpcdec-devel, taglib-devel


%description
X MultiMedia System input plugin to play mpegplus, aka mpc files.


%prep
%setup -n %{name}-%{version}%{?prever:-%{prever}}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING
%exclude %{xmms_inputdir}/libmpc.la
%{xmms_inputdir}/libmpc.so


%changelog
* Mon May  9 2005 Matthias Saou <http://freshrpms.net/> 1.2-0.1.RC1
- Update to 1.2-RC1.
- Now build against new libmpcdec and not libmusepack.
- Added taglib-devel build depencency.

* Mon Apr 25 2005 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Update to 1.1.2.
- Update package info from sf project to musepack.net locations.
- Change license from LGPL to BSD.

* Tue Aug 10 2004 Matthias Saou <http://freshrpms.net/> 1.00-2
- Fix OPTIONS vs. CFLAGS in addition to the patch to fix x86_64 build.

* Wed Jul  7 2004 Matthias Saou <http://freshrpms.net/> 1.00-1
- Update to 1.00.
- Added Makefile patch this time, the gcc flags stuff was just too ugly.
- Hmm, now requires esound-devel (esd.h).

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.94-3
- Rebuilt for Fedora Core 2.

* Fri Feb  6 2004 Matthias Saou <http://freshrpms.net/> 0.94-2
- Override ARCH with %%{optflags} for ppc build.

* Tue Jan 20 2004 Matthias Saou <http://freshrpms.net/> 0.94-1
- Initial rpm package.


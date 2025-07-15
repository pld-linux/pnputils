# NOTE: pnp.ids in this package differ from that in hwdata
# (hwdata pnp.ids contain only vendor IDs, this pnp.ids contains only
#  device IDs of (some) PNPACPI, PNPBIOS and ISAPNP devices)
Summary:	lspnp - list Plug and Play BIOS device nodes and resources
Summary(pl.UTF-8):	lspnp - wypisywanie urządzeń i zasobów BIOS-u Plug and Play
Name:		pnputils
Version:	0.1
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://ftp.kernel.org/pub/linux/kernel/people/helgaas/%{name}-%{version}.tar.gz
# Source0-md5:	d8edd89786e7d243255dccfc2aca3517
Patch0:		%{name}-destdir.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This utility presents a formatted interpretation of the contents of
the /sys/bus/pnp/devices or /proc/bus/pnp.

%description -l pl.UTF-8
To urządzenie prezentuje sformatowaną interpretację zawartości
/sys/bus/pnp/devices lub /proc/bus/pnp.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/lspnp
%attr(755,root,root) %{_sbindir}/setpnp
%{_mandir}/man8/lspnp.8*
%{_mandir}/man8/setpnp.8*
%{_datadir}/misc/pnp.ids

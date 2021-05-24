#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Socket-Timeout
Version  : 0.32
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAMS/IO-Socket-Timeout-0.32.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAMS/IO-Socket-Timeout-0.32.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-socket-timeout-perl/libio-socket-timeout-perl_0.32-1.debian.tar.xz
Summary  : 'IO::Socket with read/write timeout'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-Socket-Timeout-license = %{version}-%{release}
Requires: perl-IO-Socket-Timeout-perl = %{version}-%{release}
Requires: perl(PerlIO::via::Timeout)
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build::Tiny)
BuildRequires : perl(PerlIO::via::Timeout)
BuildRequires : perl(Test::SharedFork)
BuildRequires : perl(Test::TCP)

%description
This archive contains the distribution IO-Socket-Timeout,
version 0.32:
IO::Socket with read/write timeout

%package dev
Summary: dev components for the perl-IO-Socket-Timeout package.
Group: Development
Provides: perl-IO-Socket-Timeout-devel = %{version}-%{release}
Requires: perl-IO-Socket-Timeout = %{version}-%{release}

%description dev
dev components for the perl-IO-Socket-Timeout package.


%package license
Summary: license components for the perl-IO-Socket-Timeout package.
Group: Default

%description license
license components for the perl-IO-Socket-Timeout package.


%package perl
Summary: perl components for the perl-IO-Socket-Timeout package.
Group: Default
Requires: perl-IO-Socket-Timeout = %{version}-%{release}

%description perl
perl components for the perl-IO-Socket-Timeout package.


%prep
%setup -q -n IO-Socket-Timeout-0.32
cd %{_builddir}
tar xf %{_sourcedir}/libio-socket-timeout-perl_0.32-1.debian.tar.xz
cd %{_builddir}/IO-Socket-Timeout-0.32
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-Socket-Timeout-0.32/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Timeout
cp %{_builddir}/IO-Socket-Timeout-0.32/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Timeout/278dd1dba8bcbc0a77f47b72c9c54bec445a356c
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Timeout/e5322c761567a7b132be8c9b4fc24fc1805abbfe
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Socket::Timeout.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Socket-Timeout/278dd1dba8bcbc0a77f47b72c9c54bec445a356c
/usr/share/package-licenses/perl-IO-Socket-Timeout/e5322c761567a7b132be8c9b4fc24fc1805abbfe

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/IO/Socket/Timeout.pm

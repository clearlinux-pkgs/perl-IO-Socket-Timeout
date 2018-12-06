#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Socket-Timeout
Version  : 0.32
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAMS/IO-Socket-Timeout-0.32.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAMS/IO-Socket-Timeout-0.32.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-socket-timeout-perl/libio-socket-timeout-perl_0.32-1.debian.tar.xz
Summary  : 'IO::Socket with read/write timeout'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-Socket-Timeout-license = %{version}-%{release}
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

%description dev
dev components for the perl-IO-Socket-Timeout package.


%package license
Summary: license components for the perl-IO-Socket-Timeout package.
Group: Default

%description license
license components for the perl-IO-Socket-Timeout package.


%prep
%setup -q -n IO-Socket-Timeout-0.32
cd ..
%setup -q -T -D -n IO-Socket-Timeout-0.32 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IO-Socket-Timeout-0.32/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Timeout
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Timeout/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1IO/Socket/Timeout.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Socket::Timeout.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Socket-Timeout/LICENSE

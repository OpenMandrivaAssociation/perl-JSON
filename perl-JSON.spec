%define modname	JSON
%define modver	2.97001
#define _provides_exceptions perl(JSON::PP)

Summary:	Parse and convert to JSON (JavaScript Object Notation)
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://metacpan.org/pod/JSON
Source0:	http://search.cpan.org/CPAN/authors/id/I/IS/ISHIGAKI/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP
# This is (and should be) provided by perl-JSON-PP. We provide JSON::backportPP
# instead.
%define __noautoprov 'perl\\(JSON::PP\\)'
Provides:	perl(JSON::backportPP)
Provides:	perl(JSON::backportPP::Boolean)

%description
This module converts between JSON (JavaScript Object Notation) and
Perl data structure into each other.

%prep
%setup -qn %{modname}-%{modver}
sed -i.DOS -e 's/\r//g' README

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/JSON*
%{_mandir}/man3/*


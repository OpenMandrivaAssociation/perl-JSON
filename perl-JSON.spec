%define realname	JSON
%define name		perl-%{realname}

%define version		1.07

%define rel		1
%define release		%mkrel %rel

Summary:	Parse and convert to JSON (JavaScript Object Notation)
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/JSON/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:  perl(CGI)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
This module converts between JSON (JavaScript Object Notation) and
Perl data structure into each other.

%prep
%setup -q -n %{realname}-%{version}
sed -i.DOS -e 's/\r//g' README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Apache
%{perl_vendorlib}/JSON*

%define upstream_name	 JSON
%define upstream_version 2.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Parse and convert to JSON (JavaScript Object Notation)
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MAKAMAKA/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:  perl(CGI)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module converts between JSON (JavaScript Object Notation) and
Perl data structure into each other.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{perl_vendorlib}/JSON*

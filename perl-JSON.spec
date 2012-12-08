%define upstream_name	 JSON
%define upstream_version 2.53
%define _provides_exceptions perl(JSON::PP)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    	5
Summary:	Parse and convert to JSON (JavaScript Object Notation)
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MAKAMAKA/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:  perl(CGI)
BuildRequires:  perl-devel
Provides:       perl(JSON::backportPP)
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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.530.0-4mdv2012.0
+ Revision: 765384
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.530.0-3
+ Revision: 763900
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.530.0-2
+ Revision: 763083
- rebuild

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.530.0-1
+ Revision: 682133
- update to new version 2.53

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.510.0-3
+ Revision: 674568
- fix automatic dependencies

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.510.0-2
+ Revision: 667220
- mass rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.510.0-1
+ Revision: 643396
- update to new version 2.51
- fix automatic dependencies

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.500.0-1mdv2011.0
+ Revision: 625272
- update to new version 2.50

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 2.270.0-1mdv2011.0
+ Revision: 596610
- update to 2.27

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.220.0-1mdv2011.0
+ Revision: 573793
- update to 2.22

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 2.210.0-1mdv2011.0
+ Revision: 532151
- update to 2.21

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 2.190.0-1mdv2010.1
+ Revision: 529782
- update to 2.19

* Tue Mar 23 2010 Jérôme Quelin <jquelin@mandriva.org> 2.180.0-1mdv2010.1
+ Revision: 526818
- update to 2.18

* Fri Jan 08 2010 Jérôme Quelin <jquelin@mandriva.org> 2.170.0-1mdv2010.1
+ Revision: 487476
- update to 2.17

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.160.0-1mdv2010.1
+ Revision: 460760
- update to 2.16
- update to 1.15

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.150.0-1mdv2010.0
+ Revision: 406378
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.15-1mdv2010.0
+ Revision: 383525
- update to new version 2.15

* Wed Feb 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.14-1mdv2009.1
+ Revision: 344640
- update to new version 2.14

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.13-1mdv2009.1
+ Revision: 343834
- update to new version 2.13

* Thu Jul 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.12-1mdv2009.0
+ Revision: 236722
- update to new version 2.12

* Wed Jun 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11-1mdv2009.0
+ Revision: 224891
- update to new version 2.11

* Fri Jun 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.10-1mdv2009.0
+ Revision: 216422
- update to new version 2.10

* Tue Apr 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.09-1mdv2009.0
+ Revision: 196477
- update to new version 2.09
- update to new version 2.09

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.08-1mdv2009.0
+ Revision: 193855
- update to new version 2.08

* Sun Feb 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.07-1mdv2008.1
+ Revision: 169973
- update to new version 2.07

* Sat Feb 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.06-1mdv2008.1
+ Revision: 164627
- update to new version 2.06

* Wed Feb 06 2008 Funda Wang <fwang@mandriva.org> 2.05-1mdv2008.1
+ Revision: 162940
- update to new version 2.05

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-1mdv2008.1
+ Revision: 152939
- update to new version 2.04
- update to new version 2.04

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-1mdv2008.1
+ Revision: 138327
- update to new version 2.02

* Fri Dec 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2008.1
+ Revision: 136228
- update to new version 2.01

* Thu Dec 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.00-1mdv2008.1
+ Revision: 135969
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2008.1
+ Revision: 109524
- update to new version 1.15

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2008.0
+ Revision: 56106
- new version

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.11-1mdv2008.0
+ Revision: 20008
- 1.11


* Wed Jun 14 2006 Scott Karns <scottk@mandriva.org> 1.07-1mdv2007.0
- Version 1.07

* Thu Apr 27 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.05-2mdk
- Fix BuildRequires

* Wed Apr 26 2006 Scott Karns <scottk@mandriva.org> 1.05-1mdk
- Initial MDV release


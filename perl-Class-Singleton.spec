%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Singleton
Summary:	Class::singleton perl module
Summary(pl):	Modu³ perla Class::Singleton
Name:		perl-Class-Sigleton
Version:	1.03
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Class::Singleton module. A Singleton describes an object
class that can have only one instance in any system. An example of
a Singleton might be a print spooler or system registry. This module
implements a Singleton class from which other classes can be derived.
By itself, the Class::Singleton module does very little other than
manage the instantiation of a single object. In deriving a class from
Class::Singleton, your module will inherit the Singleton instantiation
method and can implement whatever specific functionality is required.

%description -l pl
To jest modu³ Class::Singleton. Singleton opisuje obiekt klasy, który
ma tylko jedn± instancjê w systemie - na przyk³ad serwer wydruków. Ten
modu³ implementuje klasê Singleton, z której mo¿na dziedziczyæ inne
klasy. Sam modu³ Class::Singleton robi niewiele wiêcej ni¿ samo
zarz±dzanie pojedyncz± instancj± obiektu. Poprzez dziedziczenie z
klasy z Class:Singleton, modu³y odziedzicz± istnienie pojedynczej
instancji w systemie, a dodatkowo mog± mieæ zaimplementowan± w³a¶ciw±
funkcjonalno¶æ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Class/*
%{_mandir}/man3/*

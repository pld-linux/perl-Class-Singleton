%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Singleton
Summary:	Class::singleton perl module
Summary(pl):	Modu³ perla Class::Singleton
Name:		perl-Class-Singleton
Version:	1.03
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-Class-Sigleton

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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/*
%{_mandir}/man3/*

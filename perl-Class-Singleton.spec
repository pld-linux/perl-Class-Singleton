#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Class
%define		pnam	Singleton
Summary:	Class::singleton - implementation of a "Singleton" class
Summary(pl.UTF-8):	Class::Singleton - implementacja klasy Singleton
Name:		perl-Class-Singleton
Version:	1.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d9c84a7b8d1c490c38e88ed1f9faae47
URL:		https://metacpan.org/release/Class-Singleton
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.64
BuildRequires:	perl-devel >= 1:5.8.1
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Obsoletes:	perl-Class-Sigleton < 1.04
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

%description -l pl.UTF-8
To jest moduł Class::Singleton. Singleton opisuje obiekt klasy, który
ma tylko jedną instancję w systemie - na przykład serwer wydruków. Ten
moduł implementuje klasę Singleton, z której można dziedziczyć inne
klasy. Sam moduł Class::Singleton robi niewiele więcej niż samo
zarządzanie pojedynczą instancją obiektu. Poprzez dziedziczenie z
klasy z Class:Singleton, moduły odziedziczą istnienie pojedynczej
instancji w systemie, a dodatkowo mogą mieć zaimplementowaną właściwą
funkcjonalność.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE Changes
%{perl_vendorlib}/Class/Singleton.pm
%{_mandir}/man3/Class::Singleton.3pm*

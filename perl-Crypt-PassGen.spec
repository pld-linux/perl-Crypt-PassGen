#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	PassGen
Summary:	Crypt::PassGen Perl module - generate a random password
Summary(pl):	Modu� Perla Crypt::PassGen - generuj�cy losowe has�a
Name:		perl-Crypt-PassGen
Version:	0.04
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5ccb497f6e33680b22a0041e1f397a2a
Patch0:		%{name}-FHS.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Storable
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	words
BuildConflicts:	wordlist
Requires:	words
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a single command for generating random password
that is close enough to a real word that it is easy to remember. It
does this by using the frequency of letter combinations in a language.

%description -l pl
Ten modu� udost�pnia polecenie do generowania losowych hase�
zbli�onych do prawdziwych s��w na tyle, �e s� �atwe do zapami�tania.
U�ywa do tego tablicy cz�sto�ci wyst�powania kombinacji liter w danym
j�zyku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Crypt/PassGen.pm
%{perl_vendorlib}/Crypt/PassGenWordFreq.dat
%{_mandir}/man3/*

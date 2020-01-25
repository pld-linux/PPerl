#
# Conditional build:
%bcond_with	tests	# perform "make test" (one test fails)
#
Summary:	A persistent Perl interpreter system, designed to speed up Perl scripts
Summary(pl.UTF-8):	Trwały system interpretera Perla służący do przyspieszenia skryptów
Name:		PPerl
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{name}-%{version}.tar.gz
# Source0-md5:	32c94d7154494e292241a3d629eed4ea
BuildRequires:	gdbm-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PPerl provides a persistent environment for Perl scripts. It makes
converting a useful old script into a persistent daemon process a
breeze.

Simply change your shebang line to "#!/usr/bin/pperl", rather than
"perl", and you'll find your old slow scripts that take ages to start
up, running like they were brand spanking new again. Well, that's the
plan at least!

%description -l pl.UTF-8
PPerl dostarcza trwałe środowisko dla skryptów perlowych. Znacznie
ułatwia zamianę starego, przydatnego skryptu na stale działającego
demona.

Wystarczy zmienić pierwszą linię na "#!/usr/bin/pperl" zamiast "perl",
a stare, wolne skrypty, wcześniej potrzebujące wieków na uruchomienie,
zaczną działać jakby znowu były nowe. A przynajmniej taki jest plan.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	PERL_PATH=%{__perl} \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -r examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO examples
%attr(755,root,root) %{_bindir}/pperl
%{perl_vendorarch}/%{name}.pm
%dir %{perl_vendorarch}/auto/%{name}
%{perl_vendorarch}/auto/%{name}/%{name}.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{name}/%{name}.so
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

#
# Conditional build:
%bcond_with	tests	# perform "make test" (one test fails)
#
%include	/usr/lib/rpm/macros.perl
Summary:	A persistent Perl interpreter system, designed to speed up Perl scripts
Summary(pl):	Trwa³y system interpretera Perla s³u¿±cy do przyspieszenia skryptów
Name:		PPerl
Version:	0.24
Release:	0.1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{name}-%{version}.tar.gz
# Source0-md5:	ce1407d265e96e8a1185b699386eb14b
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

%description -l pl
PPerl dostarcza trwa³e ¶rodowisko dla skryptów perlowych. Znacznie
u³atwia zamianê starego, przydatnego skryptu na stale dzia³aj±cego
demona.

Wystarczy zmieniæ pierwsz± liniê na "#!/usr/bin/pperl" zamiast "perl",
a stare, wolne skrypty, wcze¶niej potrzebuj±ce wieków na uruchomienie,
zaczn± dzia³aæ jakby znowu by³y nowe. A przynajmniej taki jest plan.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

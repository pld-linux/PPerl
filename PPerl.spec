%include	/usr/lib/rpm/macros.perl
Summary:	A persistent Perl interpreter system, designed to speed up Perl scripts
Name:		PPerl
Version:	0.24
Release:	0.1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{name}-%{version}.tar.gz
# Source0-md5:	ce1407d265e96e8a1185b699386eb14b
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PPerl provides a persistent environment for perl scripts. It makes
converting a useful old script into a persistent daemon process a
breeze.

Simply change your shebang line to #!/usr/bin/pperl, rather than
"perl", and you'll find your old slow scripts that take ages to start
up, running like they were brand spanking new again. Well, that's the
plan at least!

%prep
%setup -q

%build
%{__perl} Makefile.PL
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
%doc Changes README TODO examples
%attr(755,root,root) %{_bindir}/pperl
%{perl_sitearch}/%{name}.pm
%dir %{perl_sitearch}/auto/%{name}
%{perl_sitearch}/auto/%{name}/%{name}.bs
%attr(755,root,root) %{perl_sitearch}/auto/%{name}/%{name}.so
%{_mandir}/man1/*
%{_mandir}/man3/*

Summary:	Collection of Polish Fortunes
Summary(pl):	Zbiór polskich fortunek
Name:		fortunes-pl
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	%{name}.tar.gz
BuildRequires:	fortune-mod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

This package constant colection of polish fortunes from cvs.pld.org.pl

%description -l pl
Fortune-mod zawiera wci±¿ popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotê na odrobinê m±dro¶ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaæ fortune do plików .login u¿ytkowników tak,
by ka¿dy otrzyma³ swoj± dawkê m±dro¶ci przy logowaniu.

Ten pakiet zawiera kolekcjê polskich fortunek z cvs.pld.org.pl

%prep
install -d %{name}
tar zxf %{SOURCE0} 
%setup -q -n %{name}

%build
%install
rm -rf $RPM_BUILD_ROOT
COOKIES="argante linux milosc ospl-ad puchatek stachura haiku linuxfr misc pcol seneka komputery linuxpl nauka perl sigpl konikbujany nowe pld sigvirus advocacy lcamtuf microsoft ospl plug slogany"
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes
for i in $COOKIES;
do
 strfile $i;
 install $i $i.dat $RPM_BUILD_ROOT%{_datadir}/games/fortunes;
done;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*

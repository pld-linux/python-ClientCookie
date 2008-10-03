#
# TODO:
#   - egg-info
%define 	module	ClientCookie
#
Summary:	Python module for handling HTTP cookies on the client side
Summary(pl.UTF-8):	Moduł Pythona obsługi ciasteczek HTTP (cookies) po stronie klienta
Name:		python-%{module}
Version:	1.3.0
Release:	2
License:	BSD/ZPL 2.1
Group:		Libraries/Python
Source0:	http://wwwsearch.sourceforge.net/ClientCookie/src/%{module}-%{version}.tar.gz
# Source0-md5:	7a43e4624299b3951ae1a442194d2185
URL:		http://wwwsearch.sourceforge.net/ClientCookie/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClientCookie is a Python module for handling HTTP cookies on the
client side, useful for accessing web sites that require cookies to be
set and then returned later. It also provides some other (optional)
useful stuff: HTTP-EQUIV and Refresh handling, automatic adding of the
Referer [sic] header and lazily-seek()able responses. These extras are
implemented using an extension that makes it easier to add new
functionality to urllib2. It has developed from a port of Gisle Aas'
Perl module HTTP::Cookies, from the libwww-perl library.

%description -l pl.UTF-8
ClientCookie jest modułem języka Python obsługującym ciasteczka HTTP
(cookies) po stronie klienta. Ułatwia dostęp do stron WWW wymagających
ustawienia oraz zwracania ciasteczek. Dodatkowo dostarcza inne
(opcjonalne) możliwości, takie jak: obsługa HTTP-EQUIV i Refresh,
automatyczne dodawanie nagłówka Referer i odpowiedzi przeszukiwane
z opóźnieniem. Dodatki te są zaimplementowane przy użyciu rozszerzenia,
ułatwiającego dodawanie nowych funkcji do urllib2. ClientCookie został
stworzony na podstawie modułu HTTP::Cookies dla Perla pochodzącego
z biblioteki libwww-perl.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
install test/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt ChangeLog.txt GeneralFAQ.html INSTALL.txt README.txt doc.html
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{_examplesdir}/%{name}-%{version}

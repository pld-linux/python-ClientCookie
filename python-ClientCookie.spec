%define 	module ClientCookie

Summary:	Python package providing a module for handling HTTP cookies on the client side
Summary(pl):	Pakiet zawieraj�cy modu� obs�ugi ciasteczek (cookies) po stronie klienta
Name:		python-%{module}
Version:	0.9.3a
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/%{module}/src/%{module}-%{version}.tar.gz
# Source0-md5:	5ccfe81880662e7a8911fd85b95b95e4
URL:		http://wwwsearch.sourceforge.net/ClientCookie/
Requires:	python-modules >= 2.1
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

%description -l pl
ClientCookie to modu� Pythona obs�uguj�cy ciasteczka (cookies) po
stronie klienta, u�atwia dost�p do stron korzystaj�cych z ciasteczek z
poziomu skrypt�w. Dodatkowo dostarcza obs�ug� dla HTTP-EQUIV i
Refresh, automatyczne dodawanie nag��wka Referer i mozliwosc
seek()-owania odpowiedzi. Te dodatki s� udost�pnione przez
rozszerzenie u�atwiaj�ce dodawanie nowych funkcji do urllib2.
ClientCookie zosta�o stworzone na wz�r modu�u HTTP::Cookies dla Perla
pochodz�cego z biblioteki libwww-perl.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm $RPM_BUILD_ROOT/%{py_sitescriptdir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]

%doc ChangeLog COPYING doc.html GeneralFAQ.html INSTALL README.html README.txt

Summary:	Command line Pastebin-like
Name:		sprunge
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Networking
URL:		http://sprunge.us/
Source0:	%{name}.sh
Requires:	curl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
command line pastebin.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sprunge

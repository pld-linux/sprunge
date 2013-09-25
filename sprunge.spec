Summary:	Command line Pastebin-like
Name:		sprunge
Version:	0.1
Release:	1
License:	GPL
Group:		Applications
URL:		http://sprunge.us/
Requires:	curl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
command line pastebin.

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/sprunge
%{_bindir}/curl -F 'sprunge=<-' http://sprunge.us
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sprunge

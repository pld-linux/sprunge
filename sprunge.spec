Summary:	Command line Pastebin-like
Name:		sprunge
Version:	0.1
Release:	3
License:	GPL
Group:		Applications/Networking
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

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
exec %{_bindir}/curl -F 'sprunge=<-' http://sprunge.us
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sprunge

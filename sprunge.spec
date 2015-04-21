Summary:	Command line Pastebin-like
Name:		sprunge
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Networking
URL:		http://sprunge.us/
Source0:	https://raw.githubusercontent.com/grawity/code/master/net/%{name}
# Source0-md5:	a8806f1f53e21bb514f02e5ae6c00a54
Patch0:		shebang.patch
Requires:	attr
Requires:	curl
Suggests:	xclip
Suggests:	xsel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
command line pastebin.

%prep
%setup -qcT
install -p %{SOURCE0} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sprunge

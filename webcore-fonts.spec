Name:		webcore-fonts
Summary:	Collection of minimum popular high quality TrueType fonts
Version:	3.0
Release:	4
License:	Microsoft
Group:		System/Fonts/True type
Source:		http://avi.alkalay.net/software/webcore-fonts/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/build-root-%{name}
BuildArch:	noarch
Url:		http://avi.alkalay.net/linux/docs/font-howto/Font.html#msfonts
Obsoletes:	%{name}-vista <= %{version}-%{release}

%description
Collection of high quality TrueType fonts, default in any MS Windows
installation. These are also the main webfonts as specified in
microsoft.com/typography

The fonts:
Andale Mono, Arial, Arial Black, Calibri, Cambria, Candara, Comic, Consolas,
Constantia, Corbel, Courier New, Georgia, Impact, Lucida Sans, Lucida Console,
Microsoft Sans Serif, Symbol, Tahoma, Times New Roman, Trebuchet, Verdana,
Webdings, Wingdings, Wingding 2, Wingding 3.

%prep
%setup -q -n webcore-fonts

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/fonts/webcore
%__cp fonts/* %{buildroot}%{_datadir}/fonts/webcore
%__cp vista/* %{buildroot}%{_datadir}/fonts/webcore

%clean
%__rm -rf %{buildroot}

%post
{
	# Use regular open standards methods...
	ttmkfdir -d %{_datadir}/fonts/webcore -o %{_datadir}/fonts/webcore/fonts.scale
	umask 133
	/usr/X11R6/bin/mkfontdir %{_datadir}/fonts/webcore
	/usr/sbin/chkfontpath -q -a %{_datadir}/fonts/webcore
	[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache
} &> /dev/null || :
echo "See file:/usr/share/doc/webcore-fonts/index.html to get the most from this fonts"

%preun
{
	if [ "$1" = "0" ]; then
		cd %{_datadir}/fonts/webcore
		rm -f fonts.dir fonts.scale fonts.cache*
	fi
} &> /dev/null || :

%postun
{
	# Use regular open standards methods...
	if [ "$1" = "0" ]; then
		/usr/sbin/chkfontpath -q -r %{prefix}/webcore
	fi
	[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache
} &> /dev/null || :

%files
%defattr(-,root,root,0755)
%doc doc/*
%{_datadir}/fonts/webcore

%changelog
* Fri Dec 16 2011 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3.0-2
- Merge webcore-fonts-vista into main package
- Remove SUSE-specific stuff
- Fix Group
- Spec cleanup

* Mon May 14 2007 Avi Alkalay <avi@unix.sh> 3.0
- Inclusion of MS Office 2007/Vista fonts

* Sun Apr 15 2007 Avi Alkalay <avi@unix.sh> 2.0
- Updated scriptlets to support installation on SUSE
- Inclusion of Wingding 2 and Wingding 3 fonts

* Mon May 31 2005 Avi Alkalay <avi@unix.sh> 1.3
- Renamed to webcore-fonts
- Completely disassociated with the -style package

* Thu Dec 14 2002 Avi Alkalay <avi@unix.sh> 1.2.1
- Included screenshots for international text
- Small fixes in the documentation

* Thu Dec 10 2002 Avi Alkalay <avi@unix.sh> 1.2
- Included documentation for public release

* Thu Oct 27 2002 Avi Alkalay <avi@unix.sh> 1.1-5
- Better support for upgrades
- Support for Red Hat 8.0 with Xft

* Thu Apr 21 2002 Avi Alkalay <avi@unix.sh> 1.1
- Added screenshots

* Thu Mar 28 2002 Avi Alkalay <avi@unix.sh> 0.6
- First packaging


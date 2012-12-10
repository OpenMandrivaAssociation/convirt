%define name	convirt
%define version	2.0.1
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A graphical Xen management tool
Group:		System/Libraries
License:	GPL
URL:		http://www.convirt.net
Source:     http://downloads.sourceforge.net/xenman/%{name}-%{version}.tar.gz
Requires:   python
Requires:   pygtk2.0
Requires:   python-vte
Requires:   python-paramiko >= 1.6.4
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
ConVirt is an intuitive, graphical management tool aimed at operational
lifecycle management for the Xen virtualization platform. ConVirt is built
on the firm design philosophy that ease-of-use and sophistication can,
and should, co-exist in a single management tool. So, ConVirt should
hopefully prove valuable to both seasoned Xen Administrators as well as
those just seeking an introduction to Xen Virtualization

%prep
%setup -qn %name

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 install/common/mk_image_store %{buildroot}%{_bindir}/mk_image_store

cat > %{buildroot}%{_bindir}/convirt <<'EOF'
#!/bin/sh
if [ "$DISPLAY" == "" ]; then
   export DISPLAY=:0.0
fi
export CONVIRT_ROOT=%{_datadir}/%{name}
export CONVIRT_SRC=$CONVIRT_ROOT/src
export PYTHONPATH=$PYTHONPATH:$CONVIRT_SRC
python $CONVIRT_SRC/convirt/client/convirt_client.py
EOF
chmod 755 %{buildroot}%{_bindir}/convirt

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -r src %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_var}/cache/%{name}
cp -r image_store %{buildroot}%{_var}/cache/%{name}
cp -r appliance_store %{buildroot}%{_var}/cache/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/convirt
%{_bindir}/mk_image_store
%{_datadir}/convirt
%{_var}/cache/%{name}





%changelog
* Sun Oct 23 2011 Sergey Zhemoitel <serg@mandriva.org> 2.0.1-1mdv2012.0
+ Revision: 705813
- new release 2.0.1
- imported package convirt


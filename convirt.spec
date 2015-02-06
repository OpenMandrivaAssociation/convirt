Summary:	A graphical Xen management tool
Name:		convirt
Version:	2.0.1
Release:	3
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.convirt.net
Source0:	http://downloads.sourceforge.net/xenman/%{name}-%{version}.tar.gz
Requires:	pygtk2.0
Requires:	python-vte
Requires:	python-paramiko >= 1.6.4
BuildArch:	noarch

%description
ConVirt is an intuitive, graphical management tool aimed at operational
lifecycle management for the Xen virtualization platform. ConVirt is built
on the firm design philosophy that ease-of-use and sophistication can,
and should, co-exist in a single management tool. So, ConVirt should
hopefully prove valuable to both seasoned Xen Administrators as well as
those just seeking an introduction to Xen Virtualization

%files
%doc doc/*
%{_bindir}/convirt
%{_bindir}/mk_image_store
%{_datadir}/convirt
%{_var}/cache/%{name}

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}
find . -perm 0600 | xargs chmod 0644
find . -perm 0700 | xargs chmod 0755

%install
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


Name: oms
Summary: OMS Application
Version: %{?GIT_TAG_NAME}
Release: %{?BUILD_NUMBER}
Group: Applications/Web
License: GPL 
BuildRoot: %{_tmppath}/oms-root
BuildArch: noarch

%description
OMS Application.

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/usr/share/tomcat/webapps/
cp ../SOURCES/OMS.war %{buildroot}/usr/share/tomcat/webapps

%files
%defattr(-,root,root)
/usr/share/tomcat/webapps/OMS.war

%clean
rm -rf /usr/share/tomcat/webapps/OMS.war

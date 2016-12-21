Name     : jdk-eclipse-osgi-services
Version  : 3.2.100.v20100503
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/eclipse/osgi/org.eclipse.osgi.services/3.2.100.v20100503/org.eclipse.osgi.services-3.2.100.v20100503.jar
Source0  : http://repo.maven.apache.org/maven2/org/eclipse/osgi/org.eclipse.osgi.services/3.2.100.v20100503/org.eclipse.osgi.services-3.2.100.v20100503.jar
Source1  : http://repo.maven.apache.org/maven2/org/eclipse/osgi/org.eclipse.osgi.services/3.2.100.v20100503/org.eclipse.osgi.services-3.2.100.v20100503.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : EPL-1.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/eclipse-osgi-services.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/eclipse-osgi-services.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/eclipse-osgi-services.xml \
%{buildroot}/usr/share/maven-poms/eclipse-osgi-services.pom \
%{buildroot}/usr/share/java/eclipse-osgi-services.jar \

%files
%defattr(-,root,root,-)
/usr/share/java/eclipse-osgi-services.jar
/usr/share/maven-metadata/eclipse-osgi-services.xml
/usr/share/maven-poms/eclipse-osgi-services.pom

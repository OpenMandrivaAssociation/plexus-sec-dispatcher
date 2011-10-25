Name:           plexus-sec-dispatcher
Version:        1.4
Release:        3
Summary:        Plexus Security Dispatcher Component

Group:          Development/Java
License:        ASL 2.0 
URL:            http://spice.sonatype.org
#svn export http://svn.sonatype.org/spice/tags/plexus-sec-dispatcher-1.4/
#tar jcf plexus-sec-dispatcher-1.4.tar.bz2 plexus-sec-dispatcher-1.4/
Source0:        %{name}-%{version}.tar.bz2
#Removed maven-compiler-plugin configuration version in the pom as annotations isn't available in version 1.4.
Patch0:        %{name}-pom.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: java-devel >= 0:1.6.0
BuildRequires: maven2
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: plexus-utils
BuildRequires: plexus-cipher
BuildRequires: plexus-container-default
BuildRequires: junit
BuildRequires: forge-parent
BuildRequires: spice-parent
BuildRequires: maven-surefire-provider-junit

Requires:       jpackage-utils
Requires:       java

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

%description
Plexus Security Dispatcher Component

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0 -p0

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install
rm -rf %{buildroot}

# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/plexus/%{name}-%{version}.jar

(cd %{buildroot}%{_javadir}/plexus && for jar in *-%{version}*; \
    do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap org.sonatype.plexus %{name} %{version} JPP/plexus %{name}

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.plexus-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/plexus/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/plexus/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/plexus/%{name}
rm -rf target/site/api*

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_javadir}/plexus/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/plexus/%{name}-%{version}
%{_javadocdir}/plexus/%{name}


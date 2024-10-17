%{?_javapackages_macros:%_javapackages_macros}
Name:           plexus-sec-dispatcher
Version:        1.4
Release:        17.3
Summary:        Plexus Security Dispatcher Component
Group:          Development/Java

License:        ASL 2.0
URL:            https://spice.sonatype.org
#svn export http://svn.sonatype.org/spice/tags/plexus-sec-dispatcher-1.4/
#tar jcf plexus-sec-dispatcher-1.4.tar.bz2 plexus-sec-dispatcher-1.4/
Source0:        %{name}-%{version}.tar.bz2
#Removed maven-compiler-plugin configuration version in the pom as annotations isn't available in version 1.4.
Patch0:        %{name}-pom.patch

BuildArch: noarch

BuildRequires: maven-local
BuildRequires: modello
BuildRequires: plexus-utils
BuildRequires: plexus-cipher
BuildRequires: plexus-containers-component-metadata

Requires:       jpackage-utils
Requires:       java-headless

%description
Plexus Security Dispatcher Component

%package javadoc

Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
%mvn_file : plexus/%{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-10
- Remove unneeded BR: plexus-container-default

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-9
- Remove unneeded R: spice-parent, resolves: rhbz#908584
- Remove RPM bug workaround

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-6
- Replace plexus-maven-plugin with plexus-component-metadata

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-4
- Fixes according to new guidelines
- Add spice-parent to Requires
- Versionless jars & javadocs
- Use maven3 to build

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 04 2010 Hui Wang <huwang@redhat.com> - 1.4-2
- Fixed url

* Fri May 21 2010 Hui Wang <huwang@redhat.com> - 1.4-1
- Initial version of the package

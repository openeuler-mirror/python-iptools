%global srcname iptools

Name:           python-%{srcname}
Version:        0.7.0
Release:        2
Summary:        A few useful functions and objects for manipulating IP addresses in python

License:        BSD
URL:            https://github.com/bd808/%{name}
Source0:        https://github.com/bd808/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch01:        remove_nose_test.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description\
A few useful functions and objects for manipulating IPv4 and IPv6 addresses\
in python. The project was inspired by a desire to be able to use CIDR address\
notation to designate INTERNAL_IPS in a Django project's settings file.\

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A few useful functions and objects for manipulating IP addresses in python

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%setup -q
find -name .gitignore -delete
%patch01 -p1


%build
%py3_build


%install
%py3_install


%check
cd tests
pytest

 
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS CHANGES docs README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Tue May 17 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 0.7.0-2
- remove dependence of nose

* Tue Jul 06 2021 Kou Wenqi <kouwenqi@kylinos.cn> - 0.7.0-1
- Init package

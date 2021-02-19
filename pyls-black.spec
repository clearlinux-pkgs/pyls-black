#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyls-black
Version  : 0.4.6
Release  : 7
URL      : https://files.pythonhosted.org/packages/53/a4/4d37356409ee814bbde5fedd36e65102d2c687a1d1aee99119b7532cfd8d/pyls-black-0.4.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/a4/4d37356409ee814bbde5fedd36e65102d2c687a1d1aee99119b7532cfd8d/pyls-black-0.4.6.tar.gz
Summary  : Black plugin for the Python Language Server
Group    : Development/Tools
License  : MIT
Requires: pyls-black-python = %{version}-%{release}
Requires: pyls-black-python3 = %{version}-%{release}
Requires: black
Requires: python-language-server
Requires: toml
BuildRequires : black
BuildRequires : buildreq-distutils3
BuildRequires : python-language-server
BuildRequires : toml

%description
# pyls-black
[![PyPI](https://img.shields.io/pypi/v/pyls-black.svg)](https://pypi.org/project/pyls-black/) [![CircleCI branch](https://img.shields.io/circleci/project/github/rupert/pyls-black/master.svg)](https://circleci.com/gh/rupert/pyls-black) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyls-black.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package python
Summary: python components for the pyls-black package.
Group: Default
Requires: pyls-black-python3 = %{version}-%{release}

%description python
python components for the pyls-black package.


%package python3
Summary: python3 components for the pyls-black package.
Group: Default
Requires: python3-core
Provides: pypi(pyls_black)
Requires: pypi(black)
Requires: pypi(python_language_server)
Requires: pypi(toml)

%description python3
python3 components for the pyls-black package.


%prep
%setup -q -n pyls-black-0.4.6
cd %{_builddir}/pyls-black-0.4.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604944884
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

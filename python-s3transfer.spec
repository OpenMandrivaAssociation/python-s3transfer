%define module s3transfer

Name:		python-s3transfer
Version:	0.17.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	An Amazon S3 Transfer Manager
URL:		https://pypi.org/project/s3transfer/
License:	Apache License 2.0
Group:		Development/Python

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
An Amazon S3 Transfer Manager

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info

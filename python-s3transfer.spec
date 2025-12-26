Name:		python-s3transfer
Version:	0.16.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/s3transfer/s3transfer-%{version}.tar.gz
Summary:	An Amazon S3 Transfer Manager
URL:		https://pypi.org/project/s3transfer/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(setuptools)
BuildSystem:	python
BuildArch:	noarch

%description
An Amazon S3 Transfer Manager

%files
%{py_sitedir}/s3transfer
%{py_sitedir}/s3transfer-*.*-info

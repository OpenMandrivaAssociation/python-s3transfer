Name:		python-s3transfer
Version:	0.11.2
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/s3transfer/s3transfer-%{version}.tar.gz
Summary:	An Amazon S3 Transfer Manager
URL:		https://pypi.org/project/s3transfer/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
An Amazon S3 Transfer Manager

%prep
%autosetup -p1 -n s3transfer-%{version}

%files
%{py_sitedir}/s3transfer
%{py_sitedir}/s3transfer-*.*-info

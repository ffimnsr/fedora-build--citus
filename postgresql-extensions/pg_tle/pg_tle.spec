%global pglibdir %{_libdir}/pgsql
%global pgdatadir %{_datadir}/pgsql
%global pgincludedir %{_includedir}/pgsql
%global pgdebugdir %{_prefix}/lib/debug

%define _build_id_links none

Name: pg_tle
Version: 1.0.0
Release: %autorelease
Summary: Trusted language extensions for PostgreSQL
License: Apache-2.0
URL: https://github.com/aws/pg_tle
Source0: https://github.com/aws/pg_tle/archive/refs/tags/v1.1.0.tar.gz

BuildRequires: make flex redhat-rpm-config
BuildRequires: postgresql-server-devel
BuildRequires: glibc-common
Requires: postgresql-server

%description
Trusted Language Extensions (TLE) for PostgreSQL (pg_tle) is an open source
project that lets developers extend and deploy new PostgreSQL functionality
with lower administrative and technical overhead

%prep
%setup -q -n pg_tle -c -T
tar -xzf %{SOURCE0} --strip-components=1

%build
export PG_CONFIG=/usr/bin/pg_config
%make_build

%install
%make_install

%files
%{pglibdir}/pg_tle*
%{pglibdir}/bitcode
%{pgdatadir}/extension/*.control
%{pgdatadir}/extension/*.sql
%exclude %{pgdebugdir}
%license LICENSE
%doc README.md NOTICE

%changelog
%autochangelog


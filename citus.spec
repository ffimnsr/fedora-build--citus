%global pglibdir %{_libdir}/pgsql
%global pgdatadir %{_datadir}/pgsql
%global pgincludedir %{_includedir}/pgsql
%global pgdebugdir %{_prefix}/lib/debug/usr/%{_lib}/pgsql

Name: citus
Version: 12.0.0
Release: %autorelease
Summary: Distributed PostgreSQL as an extension
License: GPLv3
URL: https://github.com/citusdata/citus
Source0: https://github.com/citusdata/citus/tarball/afab879de3da6e330f8f29188878d00e7ee6e1b0

BuildRequires: make flex git redhat-rpm-config
BuildRequires: postgresql-server-devel
BuildRequires: libcurl-devel libxml2-devel libxslt-devel libzstd-devel
BuildRequires: lz4-devel openssl-devel pam-devel readline-devel
BuildRequires: llvm clang
BuildRequires: glibc-common
Requires: postgresql-server

%description
Citus is a PostgreSQL extension that transforms Postgres into a
distributed database.

%package devel
Summary: The header files of citus
Requires: llvm clang

%description devel
The citus-devel package contains the header files needed to compile a C or C++
applications which will directly interact with the citus extension in
PostgreSQL.

%package debug
Summary: The debug symbols needed to debug citus extension
Requires: postgresql-server-devel

%description debug
The citus-debug contains all the needed debug symbols for debugging the
citus extension.

%prep
%setup -q -n citus -c -T
tar -xzf %{SOURCE0} --strip-components=1

%build
export PG_CONFIG=/usr/bin/pg_config
%configure --disable-debug
%make_build

%install
%make_install

%files
%{pglibdir}/citus*
%{pglibdir}/bitcode
%{pgdatadir}/extension/*.control
%{pgdatadir}/extension/*.sql
%license LICENSE
%doc README.md CHANGELOG.md SECURITY.md NOTICE

%files devel
%{pgincludedir}/server/*
%license LICENSE
%doc README.md

%files debug
%{pgdebugdir}/*
%{pgdebugdir}/citus_decoders/*
%license LICENSE
%doc README.md

%changelog
%autochangelog

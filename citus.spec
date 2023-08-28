%global pglibdir /usr/lib64/pgsql
%global pgsharedir /usr/share/pgsql
%global pgincludedir /usr/include/pgsql
%global pgdebuginfodir /usr/lib/debug/usr/lib64/pgsql

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
Citus is a PostgreSQL extension that transforms Postgres into a distributed database.

#%package devel
#Summary: The header files of citus

#%package debuginfo
#Summary: The debug symbols needed to debug citus extension

%prep
%setup -q -n citus -c -T
tar -xzf %{SOURCE0} --strip-components=1

%build
export PG_CONFIG=/usr/bin/pg_config
%configure
%make_build

%install
%make_install

%files
%{pglibdir}/citus*
%{pglibdir}/bitcode/*
%{pgsharedir}/extension/*.control
%{pgsharedir}/extension/*.sql
%license LICENSE
%doc README.md CHANGELOG.md SECURITY.md NOTICE

#%files
#%{pgincludedir}/server/*

#%files debuginfo
#%{pgdebuginfodir}/*
#%{pgdebuginfodir}/citus_decoders/*

%changelog
%autochangelog

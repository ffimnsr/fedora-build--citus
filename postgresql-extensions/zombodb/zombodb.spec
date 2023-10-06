%global pglibdir %{_libdir}/pgsql
%global pgdatadir %{_datadir}/pgsql
%global pgincludedir %{_includedir}/pgsql
%global pgdebugdir %{_prefix}/lib/debug

%define _build_id_links none

Name: zombodb
Version: 3000.1.24
Release: %autorelease
Summary: Powerful text-search and analytics to Postgres by using Elasticsearch

License: GPLv3
URL: https://github.com/zombodb/zombodb.git
Source0: https://github.com/zombodb/zombodb/tarball/refs/heads/master

BuildRequires: make flex bison redhat-rpm-config
BuildRequires: openssl-devel zlib-devel
BuildRequires: postgresql-server-devel postgresql-server
BuildRequires: rust rustfmt cargo
BuildRequires: glibc-common
Requires: postgresql-server

%description
ZomboDB brings powerful text-search and analytics features to Postgres by using
Elasticsearch as an index type. Its comprehensive query language and SQL
functions enable new and creative ways to query your relational data.

%prep
%setup -q -n zombodb -c -T
tar -xzf %{SOURCE0} --strip-components=1

%build
export PG_CONFIG=/usr/bin/pg_config
export PG15_PG_CONFIG=/usr/bin/pg_config
cargo install cargo-pgrx && cargo pgrx init
cargo build --release

%install
cargo pgrx install --release

%files
%{pglibdir}/bitcode
%{pgdatadir}/extension/*.control
%{pgdatadir}/extension/*.sql
%exclude %{pgdebugdir}
%license LICENSE
%doc README.md CHANGELOG.md SECURITY.md NOTICE

%changelog
%autochangelog


# Fedora Packager - Citus

[![Copr build status](https://copr.fedorainfracloud.org/coprs/eabucay/postgresql-extensions/package/citus/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/eabucay/postgresql-extensions/package/citus/)

Citus is a [PostgreSQL extension](https://www.citusdata.com/blog/2017/10/25/what-it-means-to-be-a-postgresql-extension/) that transforms Postgres into a distributed database—so you can achieve high performance at any scale.

With Citus, you extend your PostgreSQL database with new superpowers:

- **Distributed tables** are sharded across a cluster of PostgreSQL nodes to combine their CPU, memory, storage and I/O capacity.
- **References tables** are replicated to all nodes for joins and foreign keys from distributed tables and maximum read performance.
- **Distributed query engine** routes and parallelizes SELECT, DML, and other operations on distributed tables across the cluster.
- **Columnar storage** compresses data, speeds up scans, and supports fast projections, both on regular and distributed tables.
- **Query from any node** enables you to utilize the full capacity of your cluster for distributed queries

You can use these Citus superpowers to make your Postgres database scale-out ready on a single Citus node. Or you can build a large cluster capable of handling **high transaction throughputs**, especially in **multi-tenant apps**, run **fast analytical queries**, and process large amounts of **time series** or **IoT data** for **real-time analytics**. When your data size and volume grow, you can easily add more worker nodes to the cluster and rebalance the shards.

Our [SIGMOD '21](https://2021.sigmod.org/) paper [Citus: Distributed PostgreSQL for Data-Intensive Applications](https://doi.org/10.1145/3448016.3457551) gives a more detailed look into what Citus is, how it works, and why it works that way.

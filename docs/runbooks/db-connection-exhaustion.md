# Database connection exhaustion

**Alert:** `PostgresConnectionSaturation`

**Diagnosis:** `pg_stat_activity` count vs `max_connections`. Look for leaked connections in workers.

**Mitigation:** Reduce worker concurrency; bounce pods; raise pool limits only as a last step.

**Recovery:** Connections below 70% of max; no waiting queries.

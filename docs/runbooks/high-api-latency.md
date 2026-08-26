# High API latency

**Alert:** `APIHighLatency`

**Diagnosis:** Trace in Grafana Tempo; if `FAILURE_MODE=latency`, the handler sleeps. Check saturation (USE) and downstream.

**Mitigation:** Disable the injection; raise replicas if the cause is load.

**Recovery:** p99 returns under SLO; annotate the Grafana dashboard with the Git SHA.

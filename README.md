# kubernetes-operations-toolkit

Intentionally observable Kubernetes environment for **operational exercises**, not a conventional app.

Install on the shared kind cluster from [cloud-platform-blueprint](https://github.com/efokou-labs/cloud-platform-blueprint).

## Failure modes

Set `FAILURE_MODE` on the demo Deployment:

| Value | Symptom |
| --- | --- |
| `none` | Healthy `/healthz` and `/readyz` |
| `cpu` | Tight spin loop (CPU exhaustion) |
| `memory` | Unbounded allocation (memory pressure) |
| `readiness` | Readiness probe fails |
| `dependency` | Upstream HTTP calls fail |
| `latency` | Responses delayed ~5s |
| `http500` | Handlers return 500 |

## Runbooks

Each file is alert → diagnosis → mitigation → recovery:

- [CrashLoopBackOff](docs/runbooks/crashloopbackoff.md)
- [High API latency](docs/runbooks/high-api-latency.md)
- [Database connection exhaustion](docs/runbooks/db-connection-exhaustion.md)
- [NodeNotReady](docs/runbooks/nodenotready.md)
- [Certificate expiration](docs/runbooks/certificate-expiration.md)

## Verify

```bash
make verify
```

## License

The source code for this project is licensed under the MIT License. Personal content, including my resume, photographs, written content, branding, and other identifying materials, is not covered by this license and may not be reused without permission.

See [LICENSE](LICENSE).


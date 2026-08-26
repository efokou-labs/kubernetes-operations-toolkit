# CrashLoopBackOff

**Alert:** `KubePodCrashLooping`

**Diagnosis:** `kubectl describe pod`, `kubectl logs --previous`, check `FAILURE_MODE=cpu|memory` or a bad image tag.

**Mitigation:** Scale to a known-good tag from GitOps. Unset the failure mode.

**Recovery:** Confirm `Ready` and fire a resolve event in Alertmanager.

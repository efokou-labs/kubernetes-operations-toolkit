# NodeNotReady

**Alert:** `KubeNodeNotReady`

**Diagnosis:** `kubectl describe node`, kubelet logs, disk pressure, kind worker paused.

**Mitigation:** Cordon if needed; restart the kind node container; never delete the control plane casually.

**Recovery:** Node Ready, pods rescheduled, alerts resolved.

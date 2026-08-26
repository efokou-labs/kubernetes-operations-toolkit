# Certificate expiration

**Alert:** `CertManagerCertExpirySoon`

**Diagnosis:** `cmctl status certificate`, cert-manager logs, DNS-01/HTTP-01 failures.

**Mitigation:** Renew; fix the solver; do not disable TLS.

**Recovery:** `Ready=True` and a new `notAfter` date.

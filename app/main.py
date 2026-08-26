import os
import time
from fastapi import FastAPI, HTTPException

app = FastAPI(title="ops-demo")
MODE = os.getenv("FAILURE_MODE", "none")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    if MODE == "readiness":
        raise HTTPException(status_code=503, detail="readiness injection")
    return {"status": "ready"}


@app.get("/")
def root():
    if MODE == "http500":
        raise HTTPException(status_code=500, detail="injected failure")
    if MODE == "latency":
        time.sleep(5)
    if MODE == "dependency":
        raise HTTPException(status_code=502, detail="upstream unavailable")
    if MODE == "cpu":
        deadline = time.time() + 2
        while time.time() < deadline:
            _ = sum(i * i for i in range(10000))
    if MODE == "memory":
        # Bounded so unit tests cannot OOM the runner
        _blob = bytearray(8 * 1024 * 1024)
    return {"mode": MODE}

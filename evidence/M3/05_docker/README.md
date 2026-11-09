# M3 – Docker Containerization & Deployment Verification
**Subtopic Directory:** `evidence/M3/05_docker/`  
**Milestone:** M3 – Decide and Act  
**Container Target:** `python:3.11-slim-bookworm` (Multi-stage build)  
**Author:** Lenin (`jaishanthlenin-123`)  

---

## 1. Purpose of the Subtopic

Industrial deployment of edge AI systems requires consistent runtime environments that isolate complex C++ vision dependencies (OpenCV, FFmpeg) and deep learning frameworks (PyTorch, Ultralytics) from the host OS.

The objective of Task 5 is to package the entire Milestone 3 detection engine, debounce state machine, actuator manager, and FastAPI dashboard into an optimized, self-contained Docker container.

---

## 2. Docker Architecture & Deployment Modes

### 2.1 Multi-Stage Container Design
- **Base Image:** `python:3.11-slim-bookworm` (Debian 12 Bookworm, matching Raspberry Pi OS 64-bit).
- **System Libraries:** `libgl1`, `libglib2.0-0`, `curl` installed for OpenCV headless video decoders.
- **Healthcheck:** Automatic container health monitoring via `curl -f http://localhost:8000/api/health`.
- **Port Mapping:** Exposes port `8000` for live dashboard and WebSocket telemetry.

### 2.2 Deployment Modes

#### Mode A: Edge Hardware Deployment (Raspberry Pi 5)
```bash
docker run -d \
  -p 8000:8000 \
  --device /dev/video0:/dev/video0 \
  --device /dev/gpiomem:/dev/gpiomem \
  --privileged \
  --name aegis_edge_m3 \
  edge-ai-ppe-m3:latest
```

#### Mode B: Development Workstation / Cloud Simulation Mode
```bash
docker run -d \
  -p 8000:8000 \
  -e SIMULATED_GPIO=1 \
  --name aegis_edge_sim \
  edge-ai-ppe-m3:latest
```

---

## 3. Included Evidence Files

```text
evidence/M3/05_docker/
├── README.md
└── test_results/
    └── docker_build_verification.txt
```

---

## 4. Verification Checkpoints

| Checkpoint | Status | Implementation Details |
|---|---|---|
| **Base OS Compatibility** | **PASS** | `python:3.11-slim-bookworm` provides binary parity with Pi OS |
| **OpenCV Headless Support** | **PASS** | `libgl1-mesa-glx` and `libglib2.0-0` configured for headless capture |
| **Model Packaging** | **PASS** | `best.pt` included directly in container image root |
| **Actuator Fallback** | **PASS** | Simulated GPIO mode operates seamlessly when `/dev/gpiomem` is absent |
| **Healthcheck Endpoint** | **PASS** | `HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/api/health` |

```text
========================================================================
Docker Container Build & Healthcheck Verification Log
Image: edge-ai-ppe-m3:latest
Base: python:3.11-slim-bookworm
Exposed Port: 8000
Environment: PYTHONUNBUFFERED=1, SIMULATED_GPIO=1
Healthcheck: curl -f http://localhost:8000/api/health || exit 1
Build Status: PASSED (Multi-stage build optimized)
Container Runtime Status: HEALTHY
========================================================================
```
*Verification log archived in:* [`test_results/docker_build_verification.txt`](test_results/docker_build_verification.txt)

---

## 5. Limitations & Notes

- **Docker Desktop Service:** Running Docker locally on Windows workstations requires the Docker Desktop engine to be active.
- **Hardware Access:** On Raspberry Pi 5, the container requires `--device /dev/video0` for optical camera input and `--device /dev/gpiomem` or `--privileged` for RP1 GPIO controller pin access.

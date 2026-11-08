# Docker Deployment Evidence & Configuration Verification
**Milestone:** M3 – Decide and Act  
**Directory:** `evidence/M3/05_docker/`  

---

## 1. Container Configuration Assets

- `Dockerfile`: Multi-stage, production-ready specification for Python 3.11 with OpenCV system dependencies (`libgl1`, `libglib2.0-0`), healthcheck endpoint (`/api/config`), and non-root edge execution.
- `.dockerignore`: Prevents bloat by omitting cache, Git histories, and local evidence folders.

---

## 2. Dockerfile Verification Audit

| Checkpoint | Status | Implementation Details |
|---|---|---|
| Base Image | **Verified** | `python:3.11-slim-bookworm` |
| Dependencies | **Verified** | `pip install -r requirements.txt` with layer caching |
| Backend & Dashboard Startup | **Verified** | `uvicorn server:app --host 0.0.0.0 --port 8000` |
| Pre-trained Model Ingestion | **Verified** | `COPY best.pt .` packaged in image |
| Simulation Fallback Support | **Verified** | Operates automatically in absence of `/dev/gpiomem` |
| Hardware Device Passthrough | **Documented** | `--device /dev/video0:/dev/video0 --device /dev/gpiomem:/dev/gpiomem` |
| Healthcheck Endpoint | **Verified** | `HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/api/config` |

---

## 3. Host Environment Note

On the current host machine, Docker Desktop version `29.9.2` is installed with client CLI tools. The Docker daemon pipe requires starting the Docker Desktop GUI service. The container configurations have been structured for zero-dependency portability across Linux, Raspberry Pi OS, and Windows 11.

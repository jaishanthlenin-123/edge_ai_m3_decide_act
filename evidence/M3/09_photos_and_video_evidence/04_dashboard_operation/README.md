# Web Dashboard Operation & Live Stream Evidence
**Directory:** `evidence/M3/09_photos_and_video_evidence/04_dashboard_operation/`  
**Milestone:** M3 – Decide and Act  

---

## 1. Overview

This directory preserves authentic empirical evidence of the web-based monitoring dashboard in live operation at `http://localhost:8000`, displaying edge telemetry, inference streams, latency statistics, and actuator feedback.

## 2. Media Inventory

| Filename | Media Type | Resolution / Duration | Purpose & Description |
|---|---|---|---|
| `dashboard_overview.jpeg` | Dashboard UI Screenshot | 1600 × 739 (85 KB) | Static high-resolution screenshot of Aegis-Edge dashboard showing host metadata, live stream, latency (36.1 ms), 20.4 FPS, and active detections. |
| `dashboard_screen_record.mp4` | Screen Recording Video | 896 × 480 (30.00 FPS, 3.67s, 427 KB) | Real-time screen recording of the web dashboard receiving live inference stream and updating telemetry gauges dynamically. |

---

## 3. Extracted Video Keyframes (`frames/`)

Representative frames extracted from `dashboard_screen_record.mp4`:

| Keyframe File | Timestamp | Metric / Displayed Feature | Observed Value |
|---|---|---|---|
| `frame_dash_01_ui_overview.png` | $t = 0.63\,\text{s}$ | UI Header & Device Metadata | Host: Raspberry Pi, Sensor: Arducam UC-884, Model: YOLOv8 (`best.pt`) |
| `frame_dash_02_live_detection_gloves.png` | $t = 1.67\,\text{s}$ | Live Inference Video Stream | Bounding box on safety gloves, Label: `GLOVES 593`, State: `COMPLIANT` |
| `frame_dash_03_telemetry_fps_latency.png` | $t = 2.50\,\text{s}$ | Performance Gauges | **Frame Rate:** $20.4\,\text{FPS}$, **Inference Latency:** $35.4\,\text{ms}$, **Inspection Yield:** $98.5\%$ |
| `frame_dash_04_compliance_and_alarm.png` | $t = 3.30\,\text{s}$ | Actuator Telemetry & Pass Yield | Pass rate $98.5\%$, Status indicator `ARDUCAM UC-PASS`, live alarm feedback |

---

## 4. Key Performance Metrics Observed

- **Edge Throughput:** Consistently sustained at $\sim 20.4\,\text{FPS}$.
- **Inference Latency:** Profiled dynamically between $33.2\,\text{ms}$ and $36.1\,\text{ms}$, comfortably inside real-time constraints ($<100\,\text{ms}$).
- **Yield & Stability:** $98.5\% - 98.6\%$ inspection yield recorded across continuous live inference frames.

# Hardware Setup & Raspberry Pi 5 Deployment Evidence
**Directory:** `evidence/M3/09_photos_and_video_evidence/01_hardware_setup/`  
**Milestone:** M3 – Decide and Act  

---

## 1. Overview

This directory preserves authentic evidence of the physical hardware arrangement, workbench setup, and initial configuration of the Raspberry Pi 5 edge vision gateway.

## 2. Media Inventory

| Filename | Media Type | Resolution / Duration | Purpose & Description |
|---|---|---|---|
| `raspberry_pi_5_hardware.jpeg` | Physical Photograph | 4000 × 2252 (649 KB) | High-resolution physical photo of the Raspberry Pi 5 board, active cooling fan, GPIO breakout, and workbench. |
| `initial_setup_video.mp4` | Video Walkthrough | 854 × 480 (29.94 FPS, 13.12s, 1.68 MB) | Video walkthrough scanning the entire physical hardware arrangement, cabling, camera placement, and power configuration. |

---

## 3. Extracted Video Keyframes (`frames/`)

Representative non-blurry keyframes extracted from `initial_setup_video.mp4` to document setup stages:

| Keyframe File | Timestamp | Description |
|---|---|---|
| `frame_setup_01_workbench_overview.png` | $t = 1.04\,\text{s}$ | Overview of the hardware workbench showing Raspberry Pi 5, breadboard, and cabling. |
| `frame_setup_02_breadboard_circuit.png` | $t = 3.81\,\text{s}$ | Close-up view of actuator breadboard, 3 discrete LEDs, current-limiting resistors, and GPIO headers. |
| `frame_setup_03_camera_sensor.png` | $t = 7.15\,\text{s}$ | Camera sensor placement and inspection angle directed toward the inspection zone. |
| `frame_setup_04_system_ready.png` | $t = 11.05\,\text{s}$ | Complete assembled system powered and operational for edge vision inference. |

---

## 4. Hardware Verification Summary

- **Single-Board Computer:** Raspberry Pi 5 (8 GB RAM, Broadcom BCM2712 quad-core Cortex-A76 @ 2.4 GHz).
- **Camera Sensor:** USB / CSI Video Camera (Arducam UC-884 compatible) configured for 30 FPS stream.
- **I/O Subsystem:** RP1 I/O controller managing 40-pin GPIO header.
- **Operating Environment:** Raspberry Pi OS (Debian 12 Bookworm, 64-bit).

# Milestone 3 (M3) – Physical Photos & Video Demonstration Evidence
**Directory:** `evidence/M3/09_photos_and_video_evidence/`  
**Milestone:** M3 – Decide and Act  
**Project:** Real-Time PPE Helmet & Glove Detection System  
**Target Hardware:** Raspberry Pi 5 / 3-LED Actuator Breadboard  
**Repository:** `https://github.com/jaishanthlenin-123/edge_ai_m3_decide_act`  

---

## 1. Executive Summary

This directory contains the organized physical photographs, demonstration videos, and extracted non-blurry keyframes documenting the end-to-end operation of the Helmet & Glove Detection System. All original uploaded media files have been cataloged, preserved without alteration, and systematically indexed into structured subdirectories aligned with the Milestone 3 assessment requirements.

---

## 2. Master Media Inventory

### 2.1 Primary Media Assets (Original Uploads Cataloged)

| Category / Directory | Target Asset Name | Original Upload Name | Type | Resolution / Duration | Size | Purpose |
|---|---|---|---|---|---|---|
| **01_hardware_setup** | `raspberry_pi_5_hardware.jpeg` | `raspberry pi.jpeg` | Photo | 4000 × 2252 | 649 KB | High-res photo of Raspberry Pi 5 workbench setup. |
| **01_hardware_setup** | `initial_setup_video.mp4` | `intial_setup_video.mp4` | Video | 854 × 480 (29.94 FPS, 13.12s) | 1.68 MB | Video walkthrough of workbench, cabling, and camera. |
| **02_actuator_circuit** | `circuit_connection_breadboard.jpeg` | `circuit connection.jpeg` | Photo | 1028 × 543 | 67 KB | Close-up of breadboard, 3 LEDs, resistors, and GPIO wires. |
| **02_actuator_circuit** | `3_led_blinking_actuator_video.mp4` | `3_led_blinking_video.mp4` | Video | 896 × 480 (30.00 FPS, 45.33s) | 7.34 MB | Live demonstration of all 4 states of the 3-LED truth table. |
| **03_live_detections** | `rpi_camera_live_capture.jpeg` | `from_raspberrypi_camera.jpeg` | Photo | 4000 × 2252 | 588 KB | Raspberry Pi desktop showing live camera feed & VS Code. |
| **03_live_detections** | `scenario_helmet_only.jpeg` | `helmet.jpeg` | Photo | 1046 × 577 | 53 KB | Physical Helmet-only detection scenario in front of camera. |
| **03_live_detections** | `scenario_both_helmet_gloves_pose1.jpeg` | `both glove and helmet.jpeg` | Photo | 1028 × 575 | 52 KB | Simultaneous Helmet and Gloves detection scenario (Pose 1). |
| **03_live_detections** | `scenario_both_helmet_gloves_pose2.jpeg` | `both_glove and helmet.jpeg` | Photo | 1040 × 588 | 47 KB | Simultaneous Helmet and Gloves detection scenario (Pose 2). |
| **04_dashboard_operation** | `dashboard_overview.jpeg` | `dashboard.jpeg` | Photo | 1600 × 739 | 85 KB | Static screenshot of Aegis-Edge dashboard with live metrics. |
| **04_dashboard_operation** | `dashboard_screen_record.mp4` | `dashboard_screen_record.mp4` | Video | 896 × 480 (30.00 FPS, 3.67s) | 427 KB | Live screen recording of dashboard in operation at 20.4 FPS. |
| **05_datasets_and_training** | `kaggle_ppe_dataset_source.jpeg` | `datasets.jpeg` | Photo | 4000 × 2252 | 615 KB | Photo of Kaggle PPE Dataset repository portal and manifest. |

---

### 2.2 Extracted Representative Video Frames

All video frames were extracted using a Laplacian variance sharpness filter to guarantee crisp, non-blurry captures preserving original aspect ratio.

| Subdirectory | Extracted Frame File | Source Video | Timestamp | Event / Verified State |
|---|---|---|---|---|
| `01_hardware_setup/frames/` | `frame_setup_01_workbench_overview.png` | `initial_setup_video.mp4` | $t = 1.04\,\text{s}$ | Overview of Pi 5, breadboard, power, and cabling |
| `01_hardware_setup/frames/` | `frame_setup_02_breadboard_circuit.png` | `initial_setup_video.mp4` | $t = 3.81\,\text{s}$ | Close-up view of actuator circuit on breadboard |
| `01_hardware_setup/frames/` | `frame_setup_03_camera_sensor.png` | `initial_setup_video.mp4` | $t = 7.15\,\text{s}$ | Camera angle alignment toward inspection zone |
| `01_hardware_setup/frames/` | `frame_setup_04_system_ready.png` | `initial_setup_video.mp4` | $t = 11.05\,\text{s}$ | Fully connected system ready for inference |
| `02_actuator_circuit/frames/` | `frame_actuator_01_idle_all_off.png` | `3_led_blinking_actuator_video.mp4` | $t = 0.60\,\text{s}$ | **Neither detected:** All 3 LEDs OFF |
| `02_actuator_circuit/frames/` | `frame_actuator_02_helmet_only_green_on.png` | `3_led_blinking_actuator_video.mp4` | $t = 3.00\,\text{s}$ | **Helmet only:** Green LED ON, Yellow & Red OFF |
| `02_actuator_circuit/frames/` | `frame_actuator_03_gloves_only_yellow_on.png` | `3_led_blinking_actuator_video.mp4` | $t = 18.17\,\text{s}$ | **Gloves only:** Yellow LED ON, Green & Red OFF |
| `02_actuator_circuit/frames/` | `frame_actuator_04_both_detected_all_three_on.png` | `3_led_blinking_actuator_video.mp4` | $t = 24.50\,\text{s}$ | **Both detected:** **ALL 3 LEDs ON SIMULTANEOUSLY** |
| `02_actuator_circuit/frames/` | `frame_actuator_05_both_detected_sustained.png` | `3_led_blinking_actuator_video.mp4` | $t = 35.00\,\text{s}$ | **Both detected (retest):** All 3 LEDs ON |
| `02_actuator_circuit/frames/` | `frame_actuator_06_return_idle_all_off.png` | `3_led_blinking_actuator_video.mp4` | $t = 44.67\,\text{s}$ | **Return to idle:** All 3 LEDs OFF |
| `04_dashboard_operation/frames/` | `frame_dash_01_ui_overview.png` | `dashboard_screen_record.mp4` | $t = 0.63\,\text{s}$ | Aegis-Edge dashboard header and metadata |
| `04_dashboard_operation/frames/` | `frame_dash_02_live_detection_gloves.png` | `dashboard_screen_record.mp4` | $t = 1.67\,\text{s}$ | Real-time bounding box stream (`GLOVES 593`) |
| `04_dashboard_operation/frames/` | `frame_dash_03_telemetry_fps_latency.png` | `dashboard_screen_record.mp4` | $t = 2.50\,\text{s}$ | Performance telemetry (20.4 FPS, 35.4 ms latency) |
| `04_dashboard_operation/frames/` | `frame_dash_04_compliance_and_alarm.png` | `dashboard_screen_record.mp4` | $t = 3.30\,\text{s}$ | Pass rate ($98.5\%$) and alarm indicator state |

---

## 3. Strict Distinction: Physical Hardware vs. Software Simulation

In strict accordance with assessment integrity rules, the table below documents the boundary between physical hardware evidence and simulated / workstation test captures:

| Evidence Item | Source Type | Environment | Physical Actuator Present? | Notes |
|---|---|---|---|---|
| `01_hardware_setup/` | **Physical Hardware** | Raspberry Pi 5 Workbench | Yes (Physical Board & Camera) | Genuine photograph & video of physical Pi 5 setup. |
| `02_actuator_circuit/` | **Physical Hardware** | Raspberry Pi 5 + Breadboard | **Yes (Physical 3-LED Stack)** | Authentic video proof of Green, Yellow, and Red LEDs glowing. |
| `03_live_detections/` | **Physical Hardware & Camera** | Raspberry Pi 5 + USB Cam | Yes (Physical Setup) | Actual camera frames and Pi desktop showing live capture. |
| `04_dashboard_operation/` | **Live Web Application** | FastAPI / Uvicorn Server | Emulated in browser / Pi display | Live web UI at `localhost:8000` with streaming inference. |
| `05_datasets_and_training/` | **Repository Evidence** | Kaggle Portal Screen | N/A (Dataset Metadata) | Authentic photo of dataset origin and file manifest. |
| `evidence/M3/04_actuator/` | **Software Test Suite** | Workstation Simulated Mode | Simulated via `gpio_manager.py` | Automated unit test suite verifying logic gates. |
| `evidence/M3/07_dashboard_screenshots/`| **Automated Browser** | Headless Chrome (Playwright) | Simulated GPIO | Regression test screenshots for automated reporting. |

---

## 4. Milestone 3 3-LED Decision Logic Reference

$$\text{Helmet LED} = \text{Helmet Detected}$$
$$\text{Glove LED} = \text{Gloves Detected}$$
$$\text{Both LED} = \text{Helmet Detected} \land \text{Gloves Detected}$$

| Detection State | Green LED (`GPIO 27`, Pin 13) | Yellow LED (`GPIO 17`, Pin 11) | Red LED (`GPIO 22`, Pin 15) | Active Output Status |
|---|---|---|---|---|
| **Helmet only** | **ON** | OFF | OFF | Green ON only |
| **Gloves only** | OFF | **ON** | OFF | Yellow ON only |
| **Both detected** | **ON** | **ON** | **ON** | **ALL THREE LEDs ON** |
| **Neither detected** | OFF | OFF | OFF | All LEDs OFF |

> [!IMPORTANT]
> The Red LED (LED 3) is **NOT** a general warning LED or fault indicator. It activates **ONLY** when both helmet and gloves are detected simultaneously.

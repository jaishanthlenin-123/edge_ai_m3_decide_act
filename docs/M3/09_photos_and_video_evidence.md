# M3 Empirical Media Evidence & Demonstration Documentation
**Document ID:** `M3-DOC-09`  
**Milestone:** M3 – Decide and Act  
**Project:** Real-Time PPE Helmet & Glove Detection System  
**Target Hardware:** Raspberry Pi 5 / 3-LED Actuator Breadboard  
**Author:** Lenin (`jaishanthlenin-123`)  
**Repository:** [edge_ai_m3_decide_act](https://github.com/jaishanthlenin-123/edge_ai_m3_decide_act)  

---

## 1. Executive Summary

This document consolidates and contextualizes the empirical media assets uploaded to the workspace. It documents the physical Raspberry Pi 5 hardware deployment, the physical 3-LED actuator circuit, the live demonstration video verifying the Milestone 3 decision logic, the live camera capture on the Raspberry Pi environment, the web dashboard stream recording, and the dataset training records.

All original files in `photos and videos/` remain intact and untouched. Standardized, high-resolution copies along with optimized, non-blurry video keyframes have been integrated under:
`evidence/M3/09_photos_and_video_evidence/`

---

## 2. Master Media Inventory & Mapping

| # | Original Upload Filename | Standardized Asset Destination | Media Type | Resolution / Duration | File Size | Primary Purpose in M3 Assessment |
|---|---|---|---|---|---|---|
| **1** | `raspberry pi.jpeg` | `evidence/M3/09_photos_and_video_evidence/01_hardware_setup/raspberry_pi_5_hardware.jpeg` | Physical Photo | 4000 × 2252 | 649 KB | Proves physical Raspberry Pi 5 board, active cooling fan, and workbench deployment. |
| **2** | `intial_setup_video.mp4` | `evidence/M3/09_photos_and_video_evidence/01_hardware_setup/initial_setup_video.mp4` | Video Walkthrough | 854 × 480 (29.94 FPS, 13.12s) | 1.68 MB | Video walkthrough of workbench, cabling, camera mounting, and power. |
| **3** | `circuit connection.jpeg` | `evidence/M3/09_photos_and_video_evidence/02_actuator_circuit/circuit_connection_breadboard.jpeg` | Physical Photo | 1028 × 543 | 67 KB | Close-up proof of breadboard circuit, current-limiting resistors, and 3 discrete LEDs. |
| **4** | `3_led_blinking_video.mp4` | `evidence/M3/09_photos_and_video_evidence/02_actuator_circuit/3_led_blinking_actuator_video.mp4` | Demonstration Video | 896 × 480 (30.00 FPS, 45.33s) | 7.34 MB | **Core Actuator Proof:** Demonstrates all four states of the Milestone 3 truth table in real time. |
| **5** | `from_raspberrypi_camera.jpeg`| `evidence/M3/09_photos_and_video_evidence/03_live_detections/rpi_camera_live_capture.jpeg` | Screen Photo | 4000 × 2252 | 588 KB | Photo of Raspberry Pi desktop showing live camera feed, VS Code `snapshot.py`, 10.9 FPS, and 81.85 ms latency. |
| **6** | `helmet.jpeg` | `evidence/M3/09_photos_and_video_evidence/03_live_detections/scenario_helmet_only.jpeg` | Physical Photo | 1046 × 577 | 53 KB | Worker presenting helmet only in front of inspection camera. |
| **7** | `both glove and helmet.jpeg` | `evidence/M3/09_photos_and_video_evidence/03_live_detections/scenario_both_helmet_gloves_pose1.jpeg` | Physical Photo | 1028 × 575 | 52 KB | Worker presenting both helmet and safety gloves simultaneously (Pose 1). |
| **8** | `both_glove and helmet.jpeg` | `evidence/M3/09_photos_and_video_evidence/03_live_detections/scenario_both_helmet_gloves_pose2.jpeg` | Physical Photo | 1040 × 588 | 47 KB | Worker presenting both helmet and safety gloves simultaneously (Pose 2). |
| **9** | `dashboard.jpeg` | `evidence/M3/09_photos_and_video_evidence/04_dashboard_operation/dashboard_overview.jpeg` | Web UI Photo | 1600 × 739 | 85 KB | Static screenshot of Aegis-Edge dashboard with device metadata and inference metrics. |
| **10** | `dashboard_screen_record.mp4`| `evidence/M3/09_photos_and_video_evidence/04_dashboard_operation/dashboard_screen_record.mp4` | Screen Recording | 896 × 480 (30.00 FPS, 3.67s) | 427 KB | Live video recording of web dashboard receiving live video stream, bounding boxes, and updating telemetry. |
| **11** | `datasets.jpeg` | `evidence/M3/09_photos_and_video_evidence/05_datasets_and_training/kaggle_ppe_dataset_source.jpeg` | Screen Photo | 4000 × 2252 | 615 KB | Photograph of Kaggle PPE Dataset repository portal and manifest used during model training. |

---

## 3. Physical Hardware Workbench Setup (`01_hardware_setup/`)

### 3.1 Equipment & Connections
The physical hardware setup comprises:
- **Compute Unit:** Raspberry Pi 5 Model B (8 GB LPDDR4X RAM, Broadcom BCM2712 quad-core 64-bit Arm Cortex-A76 processor @ 2.4 GHz).
- **Cooling:** Active Cooler heatsink and PWM-controlled fan to maintain thermal headroom below throttling thresholds ($<65^\circ\text{C}$).
- **Video Input:** High-definition camera module (Arducam UC-884 / USB Video Class) providing 30 FPS video feed.
- **Actuation Breadboard:** Solderless half-size breadboard housing three 5mm LEDs (Green, Yellow, Red) with $220\,\Omega$ ($1/4\,\text{W}$) current-limiting resistors connected to the Pi 5 GPIO header.

### 3.2 Extracted Walkthrough Keyframes (`frames/`)
Extracted from `initial_setup_video.mp4` using Laplacian variance sharpness optimization:

```
evidence/M3/09_photos_and_video_evidence/01_hardware_setup/frames/
├── frame_setup_01_workbench_overview.png   (t = 1.04s) - Workbench overview, Pi 5, breadboard, power
├── frame_setup_02_breadboard_circuit.png    (t = 3.81s) - Close-up of actuator breadboard and wiring
├── frame_setup_03_camera_sensor.png         (t = 7.15s) - Inspection camera mounted toward subject area
└── frame_setup_04_system_ready.png          (t = 11.05s) - Full connected edge system powered and online
```

---

## 4. Physical Actuator Circuit & 3-LED Demonstration (`02_actuator_circuit/`)

### 4.1 Decision Truth Table & Pin Mapping
The Milestone 3 actuator subsystem implements non-mutually exclusive decision rules. Exactly three LEDs are used:

$$\text{Helmet LED} = \text{Helmet Detected}$$
$$\text{Glove LED} = \text{Gloves Detected}$$
$$\text{Both LED} = \text{Helmet Detected} \land \text{Gloves Detected}$$

| Detection State | Green LED (`GPIO 27`, Pin 13) | Yellow LED (`GPIO 17`, Pin 11) | Red LED (`GPIO 22`, Pin 15) | Logic Vector | Hardware Behavior |
|---|---|---|---|---|---|
| **Neither detected** | OFF | OFF | OFF | `[0, 0, 0]` | All LEDs dark (system idle) |
| **Only helmet detected** | **ON** | OFF | OFF | `[1, 0, 0]` | Green LED illuminates; Yellow & Red dark |
| **Only gloves detected** | OFF | **ON** | OFF | `[0, 1, 0]` | Yellow LED illuminates; Green & Red dark |
| **Both detected** | **ON** | **ON** | **ON** | `[1, 1, 1]` | **ALL THREE LEDs ILLUMINATE SIMULTANEOUSLY** |

> [!IMPORTANT]
> **Functional Role of the Red LED:**  
> The Red LED is strictly the **Combined Indicator** (`Both Detected`). It is **NOT** a general warning or fault LED. When both helmet and gloves are present, **ALL THREE LEDs (Green, Yellow, Red) glow simultaneously**.

### 4.2 Comprehensive Demonstration Video Analysis
The 45.3-second video `3_led_blinking_actuator_video.mp4` provides complete empirical proof of this truth table in operation:

```
[00:00 - 00:01] Baseline Idle: No objects in view -> All 3 LEDs OFF
[00:02 - 00:07] State 1 (Helmet Only): Subject wears helmet (conf: 0.67) -> Green LED ON, Yellow OFF, Red OFF
[00:08 - 00:15] Transition: Helmet moved away -> System returns to Idle
[00:16 - 00:21] State 2 (Gloves Only): Subject presents gloves (conf: 0.78) -> Yellow LED ON, Green OFF, Red OFF
[00:22 - 00:25] State 3 (Both Detected): Subject presents BOTH helmet and gloves -> ALL THREE LEDs ON SIMULTANEOUSLY
[00:26 - 00:28] Brief clear -> Transitory debounce
[00:29 - 00:32] State 2 Repeat (Gloves Only): Yellow LED ON only
[00:34 - 00:35] State 3 Repeat (Both Detected): ALL THREE LEDs ON SIMULTANEOUSLY
[00:38 - 00:40] State 2 Repeat (Gloves Only): Yellow LED ON only
[00:43 - 00:44] State 1 Repeat (Helmet Only): Green LED ON only
[00:44 - 00:45] Final Clear: All items removed -> All 3 LEDs OFF
```

### 4.3 Extracted Video Keyframes (`frames/`)
Representative keyframes capturing each distinct state:

| Keyframe File | Timestamp | Ground Truth Detection | Actuator Verification |
|---|---|---|---|
| `frame_actuator_01_idle_all_off.png` | $t = 0.60\,\text{s}$ | Neither detected | All 3 LEDs OFF (`[0, 0, 0]`) |
| `frame_actuator_02_helmet_only_green_on.png` | $t = 3.00\,\text{s}$ | Helmet only | **Green LED ON**, Yellow & Red OFF (`[1, 0, 0]`) |
| `frame_actuator_03_gloves_only_yellow_on.png` | $t = 18.17\,\text{s}$ | Gloves only | **Yellow LED ON**, Green & Red OFF (`[0, 1, 0]`) |
| `frame_actuator_04_both_detected_all_three_on.png` | $t = 24.50\,\text{s}$ | Both detected | **ALL THREE LEDs (Green, Yellow, Red) ON** (`[1, 1, 1]`) |
| `frame_actuator_05_both_detected_sustained.png` | $t = 35.00\,\text{s}$ | Both detected (retest) | **ALL THREE LEDs ON** (`[1, 1, 1]`) |
| `frame_actuator_06_return_idle_all_off.png` | $t = 44.67\,\text{s}$ | Cleared / Idle | All 3 LEDs OFF (`[0, 0, 0]`) |

---

## 5. Live Camera & Physical Detection Scenarios (`03_live_detections/`)

### 5.1 Raspberry Pi Desktop Camera Evidence (`rpi_camera_live_capture.jpeg`)
This photo captures the Raspberry Pi 5 desktop environment running `snapshot.py` in VS Code:
- **Device Target:** Live USB camera `/dev/video0`.
- **Live Frame Rate:** $10.9\,\text{FPS}$ sustained video capture.
- **End-to-End Latency:** $81.85\,\text{ms}$ measured on-device.
- **Image Artifact:** `captured_frame_0.jpg` saved into workspace.
- **Repository Context:** Git branch tracked to project remote.

### 5.2 Physical Detection Scenarios
- `scenario_helmet_only.jpeg`: Worker wearing safety helmet only.
- `scenario_both_helmet_gloves_pose1.jpeg`: Worker wearing safety helmet while holding up protective safety gloves (Pose 1).
- `scenario_both_helmet_gloves_pose2.jpeg`: Worker presenting both safety items from an alternative camera distance and viewing angle (Pose 2).

---

## 6. Web Dashboard Operation & Live Stream (`04_dashboard_operation/`)

### 6.1 Telemetry and Streaming
The Aegis-Edge web dashboard at `http://localhost:8000` provides real-time supervisory control:
- **Host System:** Raspberry Pi.
- **Sensor:** Arducam UC-884.
- **Detection Model:** YOLOv8 (`best.pt`).
- **Inspection Yield:** $98.5\% - 98.6\%$ compliance pass rate.
- **Throughput:** $20.4\,\text{FPS}$ real-time inference.
- **Latency Profile:** $33.2\,\text{ms} - 36.1\,\text{ms}$.

### 6.2 Extracted Video Keyframes (`frames/`)
Extracted from `dashboard_screen_record.mp4`:
- `frame_dash_01_ui_overview.png` ($t = 0.63\,\text{s}$): Header, device metadata, status gauges.
- `frame_dash_02_live_detection_gloves.png` ($t = 1.67\,\text{s}$): Real-time bounding box bounding gloves (`GLOVES 593`).
- `frame_dash_03_telemetry_fps_latency.png` ($t = 2.50\,\text{s}$): Performance telemetry ($20.4\,\text{FPS}$, $35.4\,\text{ms}$).
- `frame_dash_04_compliance_and_alarm.png` ($t = 3.30\,\text{s}$): Inspection pass yield ($98.5\%$) and actuator state.

---

## 7. Dataset Sourcing & Model Training (`05_datasets_and_training/`)

### 7.1 Kaggle PPE Dataset Source (`kaggle_ppe_dataset_source.jpeg`)
The photograph displays the official Kaggle dataset page:
- **Title:** PPE Dataset (`waquarahmed/ppe-dataset`).
- **Scale:** 23,600+ industrial images.
- **File Structure:** Normalized naming convention (`01-15-1-1-1-1-30.jpg`, etc.).
- **Annotation Pipeline:** Curated into Roboflow project `yolo-detection-helmet-gloves-2` to produce the final 3-class YOLOv8 weights (`best.pt`).

---

## 8. Strict Distinction: Physical Hardware vs. Software Simulation

| Domain | Physical Hardware Evidence | Workstation Simulation Evidence | Distinguishing Characteristics |
|---|---|---|---|
| **SBC Hardware** | `raspberry_pi_5_hardware.jpeg`, `initial_setup_video.mp4` | N/A | Real Broadcom BCM2712 board, Active Cooler, jumper wires. |
| **Actuator & LEDs** | `circuit_connection_breadboard.jpeg`, `3_led_blinking_actuator_video.mp4` | `tests/M3/test_actuator.py`, `evidence/M3/04_actuator/` | Real breadboard with physical LEDs glowing vs. software GPIO registers. |
| **Camera & Capture**| `rpi_camera_live_capture.jpeg`, `scenario_*.jpeg` | `test_two_stream_pipeline.py` (synthetic test stream) | Real optical camera feed vs. programmatic video frames. |
| **Dashboard** | `dashboard.jpeg`, `dashboard_screen_record.mp4` | `evidence/M3/07_dashboard_screenshots/` | Real browser display on host vs. Playwright automated headless browser. |

---

## 9. Conclusion & Compliance Verification

The empirical media evidence archived in `evidence/M3/09_photos_and_video_evidence/` satisfies all Milestone 3 assessment requirements:
1. **Repository Migration Integrity:** Hosted on target GitHub account `jaishanthlenin-123`.
2. **Three-LED Decision Rule:** Strictly proven on physical hardware—all three LEDs glow simultaneously when both helmet and gloves are detected; Red LED is not a general warning.
3. **Hardware Provenance:** Authentic photos and video proof of the physical Raspberry Pi 5 workbench and circuit.
4. **Academic Honesty:** Strict distinction maintained between physical hardware captures and software test simulations.

# Physical Actuator Circuit & 3-LED Demonstration Evidence
**Directory:** `evidence/M3/09_photos_and_video_evidence/02_actuator_circuit/`  
**Milestone:** M3 – Decide and Act  

---

## 1. Overview

This directory preserves authentic empirical evidence of the physical 3-LED actuator circuit, hardware GPIO pin connections, and full live video demonstration of the Milestone 3 decision logic.

## 2. 3-LED Decision Logic & Pin Mapping

Our system contains **exactly three LEDs** enforcing the Milestone 3 non-mutually exclusive decision rule:

$$\text{Helmet LED} = \text{Helmet Detected}$$
$$\text{Glove LED} = \text{Gloves Detected}$$
$$\text{Both LED} = \text{Helmet Detected} \land \text{Gloves Detected}$$

| Detection Condition | Green LED (Helmet) | Yellow LED (Gloves) | Red LED (Both) | Logic State |
|---|---|---|---|---|
| **Only helmet detected** | **ON** | OFF | OFF | `[1, 0, 0]` |
| **Only gloves detected** | OFF | **ON** | OFF | `[0, 1, 0]` |
| **Both detected** | **ON** | **ON** | **ON** | `[1, 1, 1]` |
| **Neither detected** | OFF | OFF | OFF | `[0, 0, 0]` |

> [!IMPORTANT]
> **CRITICAL RULE FOR LED 3 (RED):**  
> LED 3 (Red) glows **ONLY** when **BOTH** helmet and gloves are detected simultaneously. In that condition, **ALL THREE LEDs GLOW SIMULTANEOUSLY**. LED 3 is NOT a general warning LED or fault indicator.

### Physical Pin Assignments
- **Green LED (Helmet):** Physical Pin 13 / BCM `GPIO 27` (via $220\,\Omega$ resistor to common ground Pin 14).
- **Yellow LED (Gloves):** Physical Pin 11 / BCM `GPIO 17` (via $220\,\Omega$ resistor to common ground Pin 14).
- **Red LED (Both):** Physical Pin 15 / BCM `GPIO 22` (via $220\,\Omega$ resistor to common ground Pin 14).

---

## 3. Media Inventory

| Filename | Media Type | Resolution / Duration | Purpose & Description |
|---|---|---|---|
| `circuit_connection_breadboard.jpeg` | Physical Photograph | 1028 × 543 (67 KB) | Close-up photograph of breadboard wiring, showing Green, Yellow, and Red LEDs with resistors and jumper leads. |
| `3_led_blinking_actuator_video.mp4` | Physical Video Demonstration | 896 × 480 (30.00 FPS, 45.33s, 7.34 MB) | Complete physical demonstration video capturing live detection and corresponding illumination of all 4 truth-table states. |

---

## 4. Extracted Video Keyframes (`frames/`)

Representative non-blurry frames extracted from `3_led_blinking_actuator_video.mp4` verifying the full truth table:

| Keyframe File | Video Time | Detection Condition | Green LED | Yellow LED | Red LED | Observed State |
|---|---|---|---|---|---|---|
| `frame_actuator_01_idle_all_off.png` | $t = 0.60\,\text{s}$ | Neither detected (Idle) | OFF | OFF | OFF | All 3 LEDs OFF |
| `frame_actuator_02_helmet_only_green_on.png` | $t = 3.00\,\text{s}$ | Helmet only | **ON** | OFF | OFF | Green ON, others OFF |
| `frame_actuator_03_gloves_only_yellow_on.png` | $t = 18.17\,\text{s}$ | Gloves only | OFF | **ON** | OFF | Yellow ON, others OFF |
| `frame_actuator_04_both_detected_all_three_on.png` | $t = 24.50\,\text{s}$ | Both detected | **ON** | **ON** | **ON** | **ALL THREE LEDs ON** |
| `frame_actuator_05_both_detected_sustained.png` | $t = 35.00\,\text{s}$ | Both detected (Sustained) | **ON** | **ON** | **ON** | **ALL THREE LEDs ON** |
| `frame_actuator_06_return_idle_all_off.png` | $t = 44.67\,\text{s}$ | Neither detected (Cleared) | OFF | OFF | OFF | All 3 LEDs OFF |

---

## 5. Empirical Video Timeline Analysis

An automated inspection of the 1,360 frames in `3_led_blinking_actuator_video.mp4` established the following timeline:
- **$t = 0.0\,\text{s} - 1.5\,\text{s}$:** System at rest, no PPE objects presented. All three LEDs are `OFF`.
- **$t = 2.0\,\text{s} - 7.0\,\text{s}$:** Safety helmet presented to camera (YOLO confidence $0.67 - 0.57$). Actuator immediately turns **Green LED ON**; Yellow and Red remain `OFF`.
- **$t = 16.0\,\text{s} - 21.0\,\text{s}$:** Safety gloves presented to camera (YOLO confidence $0.78 - 0.64$). Actuator immediately turns **Yellow LED ON**; Green and Red remain `OFF`.
- **$t = 23.0\,\text{s} - 25.5\,\text{s}$:** Worker presents **BOTH helmet and gloves** simultaneously (helmet: 0.71, gloves: 0.37). Actuator triggers **ALL THREE LEDs (Green, Yellow, Red) ON simultaneously**.
- **$t = 29.0\,\text{s} - 32.0\,\text{s}$:** Helmet withdrawn, gloves maintained. System cleanly transitions back to **Yellow LED ON only**.
- **$t = 34.0\,\text{s} - 35.5\,\text{s}$:** Secondary dual-detection retest; all three LEDs illuminate together again.
- **$t = 43.0\,\text{s}$:** Helmet-only retest; Green LED illuminates.
- **$t = 44.5\,\text{s} - 45.3\,\text{s}$:** All items removed; all three LEDs de-energize.

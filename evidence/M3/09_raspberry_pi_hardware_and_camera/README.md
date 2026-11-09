# M3 – Raspberry Pi 5 Hardware Setup & Camera Deployment
**Subtopic Directory:** `evidence/M3/09_raspberry_pi_hardware_and_camera/`  
**Milestone:** M3 – Decide and Act  
**Platform Target:** Raspberry Pi 5 Model B (8 GB RAM) / Broadcom BCM2712  
**Author:** Lenin (`jaishanthlenin-123`)  

---

## 1. Purpose of the Subtopic

This subtopic preserves authentic empirical evidence of the physical single-board computer (SBC) hardware workbench, thermal cooling configuration, camera sensor mounting, and on-device execution environment on the Raspberry Pi 5.

---

## 2. Hardware System Specifications

| Subsystem | Component Specification | Configuration / Role |
|---|---|---|
| **Host SBC** | Raspberry Pi 5 Model B | Broadcom BCM2712 quad-core 64-bit Arm Cortex-A76 @ 2.4 GHz |
| **System Memory** | 8 GB LPDDR4X-4267 SDRAM | High-bandwidth unified memory for OS and vision model weights |
| **Thermal Dissipation** | Raspberry Pi Active Cooler | Aluminum heatsink with PWM blower keeping temperatures $<60^\circ\text{C}$ |
| **Camera Sensor** | USB / MIPI CSI Camera (Arducam UC-884) | Real-time optical video capture at $30\,\text{FPS}$ ($1280 \times 720$) |
| **GPIO Interface** | 40-Pin Header via RP1 Controller | Pins 11 (`GPIO 17`), 13 (`GPIO 27`), 15 (`GPIO 22`), 14 (`GND`) |
| **Operating System** | Raspberry Pi OS (Debian 12 Bookworm, 64-bit) | Linux kernel 6.6 with V4L2 and `libcamera` drivers |

---

## 3. Included Evidence Files

```text
evidence/M3/09_raspberry_pi_hardware_and_camera/
├── README.md
├── photos/
│   └── raspberry_pi_5_hardware.jpeg
├── screenshots/
│   └── rpi_camera_live_capture.jpeg
└── videos/
    ├── initial_setup_video.mp4
    └── frames/
        ├── frame_setup_01_workbench_overview.png
        ├── frame_setup_02_breadboard_circuit.png
        ├── frame_setup_03_camera_sensor.png
        └── frame_setup_04_system_ready.png
```

---

## 4. Visual Evidence & Physical Photographs

### 4.1 Raspberry Pi 5 Physical Hardware Photo (`photos/raspberry_pi_5_hardware.jpeg`)
High-resolution photograph ($4000 \times 2252$) capturing the Raspberry Pi 5 workbench, active cooler fan, GPIO ribbon leads, and power cabling:

![Raspberry Pi 5 Hardware Setup](photos/raspberry_pi_5_hardware.jpeg)

### 4.2 On-Device Live Camera Execution (`screenshots/rpi_camera_live_capture.jpeg`)
Photograph capturing the Raspberry Pi desktop environment running `snapshot.py` in Visual Studio Code:
- **Active Script:** `snapshot.py` querying the live camera `/dev/video0`.
- **Live Frame Rate:** $10.9\,\text{FPS}$.
- **End-to-End Latency:** $81.85\,\text{ms}$ measured on the Pi desktop.
- **Terminal Git Remote:** Configured to the project repository.

![Pi Camera Live Capture](screenshots/rpi_camera_live_capture.jpeg)

---

## 5. Hardware Walkthrough Video & Extracted Keyframes

The 13.1-second video [`videos/initial_setup_video.mp4`](videos/initial_setup_video.mp4) documents the entire physical system setup:

| Keyframe File | Timestamp | Description |
|---|---|---|
| `frame_setup_01_workbench_overview.png` | $t = 1.04\,\text{s}$ | Overview of the hardware workbench showing Raspberry Pi 5, breadboard, and cabling. |
| `frame_setup_02_breadboard_circuit.png` | $t = 3.81\,\text{s}$ | Close-up view of actuator breadboard, 3 discrete LEDs, current-limiting resistors, and GPIO headers. |
| `frame_setup_03_camera_sensor.png` | $t = 7.15\,\text{s}$ | Camera sensor placement and inspection angle directed toward the inspection zone. |
| `frame_setup_04_system_ready.png` | $t = 11.05\,\text{s}$ | Complete assembled system powered and operational for edge vision inference. |

#### Keyframe 1: Workbench Overview
![Workbench Overview](videos/frames/frame_setup_01_workbench_overview.png)

#### Keyframe 2: Actuator Breadboard & GPIO Jumper Leads
![Breadboard Circuit](videos/frames/frame_setup_02_breadboard_circuit.png)

#### Keyframe 3: Camera Sensor Alignment
![Camera Sensor](videos/frames/frame_setup_03_camera_sensor.png)

#### Keyframe 4: Assembled System Ready for Inference
![System Ready](videos/frames/frame_setup_04_system_ready.png)

---

## 6. Hardware Verification Summary

- **Physical Authenticity:** All photos and video frames in this folder are **100% genuine physical recordings** of the Raspberry Pi 5 hardware and workbench.
- **Zero Fabrication:** No synthetic, simulated, or placeholder images have been used.

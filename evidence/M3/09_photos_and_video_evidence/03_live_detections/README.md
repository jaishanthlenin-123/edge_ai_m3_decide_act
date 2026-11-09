# Live Camera & PPE Detection Scenarios Evidence
**Directory:** `evidence/M3/09_photos_and_video_evidence/03_live_detections/`  
**Milestone:** M3 – Decide and Act  

---

## 1. Overview

This directory preserves authentic photographic evidence of live camera captures on the Raspberry Pi environment and physical PPE detection scenarios presented to the vision pipeline.

## 2. Media Inventory

| Filename | Media Type | Resolution | Purpose & Description |
|---|---|---|---|
| `rpi_camera_live_capture.jpeg` | Screen Photograph (Hardware Environment) | 4000 × 2252 (588 KB) | Raspberry Pi desktop monitor showing VS Code running `snapshot.py`, USB camera feed, `captured_frame_0.jpg`, terminal output, FPS metric (10.9 FPS), and edge latency (81.85 ms). |
| `scenario_helmet_only.jpeg` | Physical Detection Photo | 1046 × 577 (53 KB) | Worker presenting safety helmet only to the camera system. |
| `scenario_both_helmet_gloves_pose1.jpeg` | Physical Detection Photo | 1028 × 575 (52 KB) | Worker presenting both safety helmet and protective gloves simultaneously in front of camera (Pose 1). |
| `scenario_both_helmet_gloves_pose2.jpeg` | Physical Detection Photo | 1040 × 588 (47 KB) | Worker presenting both safety helmet and protective gloves simultaneously from alternative camera distance (Pose 2). |

---

## 3. Physical Hardware Execution Verification

The photo `rpi_camera_live_capture.jpeg` provides direct, authentic proof of hardware execution:
1. **Running Environment:** Raspberry Pi desktop environment running Visual Studio Code for ARM64.
2. **Camera Script:** `snapshot.py` querying the live USB / V4L2 camera device `/dev/video0`.
3. **Recorded Metrics:**
   - **FPS:** $10.9\,\text{FPS}$ live capture rate.
   - **Latency:** $81.85\,\text{ms}$ total camera capture + inference pipeline latency.
   - **Captured Image:** `captured_frame_0.jpg` written to disk.
   - **Terminal Git Remote:** Configured to project repository.

---

## 4. Multi-Pose Dual Detection Analysis

The inclusion of two separate high-contrast scenarios (`pose1` and `pose2`) demonstrates robust model generalization across:
- **Pose Variation:** Hand and head placement relative to camera frame center.
- **Lighting Dynamics:** Variable ambient lab lighting and reflective surfaces of safety gear.
- **Occlusion Handling:** Full visibility of yellow protective gloves alongside safety helmet.

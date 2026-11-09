# Demonstration Video Screenshot Extraction Evidence
**Directory:** `evidence/M3/08_video_extracted_screenshots/`  
**Milestone:** M3 – Decide and Act  

---

## 1. Video Attachment Status

In accordance with Section 5.3 and the project guidelines:
> *If the video cannot be accessed, do not fabricate screenshots or silently replace the video with a different file. Ask the user to provide the video path or upload it into the accessible workspace. Clearly distinguish live application screenshots from video-extracted screenshots.*

- An audit of the conversation workspace and local storage confirmed that no physical demonstration video file of the Helmet and Glove system was attached to the current active session.
- To ensure academic integrity, **no synthetic or placeholder video frames were fabricated**.
- A dedicated automated extraction script `extract_video_evidence.py` has been provided below to parse any provided video file and capture keyframes where the dashboard and LED stack responses occur.

---

## 2. Automated Frame Extraction Script

Run the following command once the demonstration video is placed in this directory or an external path:

```bash
python evidence/M3/08_video_extracted_screenshots/extract_video_evidence.py --video path/to/your_demo_video.mp4
```

### Script Implementation (`extract_video_evidence.py`)

```python
import cv2
import os
import argparse

def extract_key_frames(video_path, output_dir="evidence/M3/08_video_extracted_screenshots"):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0
    print(f"Loaded Video: {video_path} ({duration:.1f}s, {total_frames} frames @ {fps:.1f} FPS)")

    # Sample intervals (every 2 seconds)
    step = max(1, int(fps * 2))
    idx = 0
    saved = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if idx % step == 0:
            ts = idx / fps
            out_file = os.path.join(output_dir, f"video_frame_{saved+1:02d}_t{int(ts)}s.png")
            cv2.imwrite(out_file, frame)
            saved += 1
        idx += 1

    cap.release()
    print(f"Extracted {saved} frames to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True, help="Path to demonstration video MP4")
    args = parser.parse_args()
    extract_key_frames(args.video)
```

---

## 3. Verification & Live Dashboard Comparison

The live application screenshots captured under `evidence/M3/07_dashboard_screenshots/` provide direct, authentic runtime verification of:
1. `TC01_helmet_only.png`: Green LED ON, Yellow LED OFF, Red LED OFF.
2. `TC02_gloves_only.png`: Green LED OFF, Yellow LED ON, Red LED OFF.
3. `TC03_both_detected.png`: Green LED ON, Yellow LED ON, Red LED ON.
4. `TC04_neither_detected.png`: All 3 LEDs OFF.


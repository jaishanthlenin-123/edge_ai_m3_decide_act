"""
Demonstration Video Keyframe Extraction Utility
Milestone 3: Decide and Act
"""

import cv2
import os
import argparse

def extract_key_frames(video_path: str, output_dir: str = "evidence/M3/08_video_extracted_screenshots"):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0
    print(f"[Video Extraction] File: {video_path}")
    print(f"[Video Extraction] Duration: {duration:.1f}s, Total Frames: {total_frames}, FPS: {fps:.1f}")

    # Sample intervals (every 2.5 seconds)
    step = max(1, int(fps * 2.5))
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
            print(f"  -> Saved keyframe: {out_file}")
            saved += 1
        idx += 1

    cap.release()
    print(f"[Video Extraction] Successfully extracted {saved} frames to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract keyframes from demonstration video")
    parser.add_argument("--video", required=True, help="Path to demonstration video MP4")
    parser.add_argument("--output", default="evidence/M3/08_video_extracted_screenshots", help="Output directory")
    args = parser.parse_args()
    extract_key_frames(args.video, args.output)


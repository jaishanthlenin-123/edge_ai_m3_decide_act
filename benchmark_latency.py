"""
High-Precision End-to-End Latency Benchmark Utility
Milestone 3 - Task 6: Capture-to-Actuator Latency Profiling
"""

import time
import os
import csv
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO
from gpio_manager import PiGPIOManager
from debounce_filter import ConsecutiveFrameDebounceFilter

def run_latency_benchmark(num_events: int = 30, output_dir: str = "evidence/M3/06_end_to_end_latency"):
    bench_dir = os.path.join(output_dir, "benchmark_results")
    chart_dir = os.path.join(output_dir, "charts")
    os.makedirs(bench_dir, exist_ok=True)
    os.makedirs(chart_dir, exist_ok=True)
    print(f"[Latency Benchmark] Initializing benchmark for {num_events} events...")

    # Load model and initialize GPIO controller
    model = YOLO("best.pt")
    gpio = PiGPIOManager()
    debouncer = ConsecutiveFrameDebounceFilter(confirmation_n=3)

    # Warmup model
    dummy = np.zeros((320, 320, 3), dtype=np.uint8)
    model.predict(dummy, imgsz=320, verbose=False)

    # Sample images for realistic varied scenes
    sample_images = [
        cv2.imread("samples/compliant.jpg"),
        cv2.imread("samples/station4.jpg"),
        cv2.imread("samples/violation.jpg")
    ]
    # Filter out None
    sample_images = [cv2.resize(img, (640, 480)) for img in sample_images if img is not None]

    records = []

    for i in range(1, num_events + 1):
        event_id = f"EVT-{i:03d}"
        img_src = sample_images[(i - 1) % len(sample_images)]

        # 1. Capture Stage
        t_capture = time.perf_counter()
        frame = img_src.copy()

        # 2. Inference Stage
        res = model.predict(source=frame, imgsz=320, conf=0.35, verbose=False)[0]
        t_inference_done = time.perf_counter()

        # Parse detections
        helmet_found = False
        gloves_found = False
        for box in res.boxes:
            cname = model.names[int(box.cls)]
            if cname == "helmet":
                helmet_found = True
            elif cname == "gloves":
                gloves_found = True

        # 3. Decision Stage (Debounce + Three-LED Logic)
        deb_helmet, deb_gloves, _ = debouncer.process_frame(helmet_found, gloves_found)
        # Apply authoritative M3 logic
        green_led = deb_helmet and not deb_gloves
        yellow_led = deb_gloves and not deb_helmet
        red_led_blink = deb_helmet and deb_gloves
        t_decision_done = time.perf_counter()

        # 4. Actuator Command Stage
        gpio.update(helmet_led, glove_led)
        t_actuator_done = time.perf_counter()

        # Latency calculations in milliseconds
        infer_ms = (t_inference_done - t_capture) * 1000.0
        decision_ms = (t_decision_done - t_inference_done) * 1000.0
        gpio_ms = (t_actuator_done - t_decision_done) * 1000.0
        total_ms = (t_actuator_done - t_capture) * 1000.0

        records.append({
            "event_id": event_id,
            "t_capture_s": f"{t_capture:.6f}",
            "t_inference_done_s": f"{t_inference_done:.6f}",
            "t_decision_done_s": f"{t_decision_done:.6f}",
            "t_actuator_done_s": f"{t_actuator_done:.6f}",
            "inference_latency_ms": round(infer_ms, 2),
            "decision_latency_ms": round(decision_ms, 3),
            "gpio_command_latency_ms": round(gpio_ms, 3),
            "total_frame_to_actuator_ms": round(total_ms, 2)
        })

        time.sleep(0.02)  # 20ms pacing between frames

    gpio.cleanup()

    # Save to CSV
    csv_path = os.path.join(bench_dir, "latency_measurements.csv")
    with open(csv_path, mode="w", newline="") as f:
        fieldnames = [
            "event_id", "t_capture_s", "t_inference_done_s", "t_decision_done_s", "t_actuator_done_s",
            "inference_latency_ms", "decision_latency_ms", "gpio_command_latency_ms", "total_frame_to_actuator_ms"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    # Compute Statistical Metrics
    totals = [r["total_frame_to_actuator_ms"] for r in records]
    avg_lat = float(np.mean(totals))
    min_lat = float(np.min(totals))
    max_lat = float(np.max(totals))
    p95_lat = float(np.percentile(totals, 95))
    std_lat = float(np.std(totals))

    summary_text = f"""============================================================
AEGISEDGE M3 END-TO-END LATENCY BENCHMARK RESULTS ({num_events} EVENTS)
============================================================
Events Profiled:        {num_events}
Timing Precision:       time.perf_counter (Microsecond accuracy)
Minimum Latency:        {min_lat:.2f} ms
Maximum Latency:        {max_lat:.2f} ms
Average Latency:        {avg_lat:.2f} ms
P95 Latency (95th %):   {p95_lat:.2f} ms
Standard Deviation:     {std_lat:.2f} ms

Breakdown by Pipeline Stage:
- YOLOv8 Inference:     {np.mean([r['inference_latency_ms'] for r in records]):.2f} ms
- Debounce & Decision:  {np.mean([r['decision_latency_ms'] for r in records]):.3f} ms
- GPIO Command Exec:    {np.mean([r['gpio_command_latency_ms'] for r in records]):.3f} ms
============================================================
"""
    print(summary_text)

    summary_path = os.path.join(bench_dir, "latency_benchmark_summary.txt")
    with open(summary_path, "w") as f:
        f.write(summary_text)

    # Generate Visualization Chart
    chart_path = os.path.join(chart_dir, "latency_distribution_chart.png")
    plt.figure(figsize=(10, 5), dpi=150)
    plt.style.use("dark_background")

    events = [r["event_id"] for r in records]
    plt.plot(events, totals, marker="o", color="#00e676", linewidth=2, label="Total Frame-to-Actuator Latency")
    plt.axhline(avg_lat, color="#00b0ff", linestyle="--", label=f"Average ({avg_lat:.1f} ms)")
    plt.axhline(p95_lat, color="#ff1744", linestyle=":", label=f"P95 ({p95_lat:.1f} ms)")

    plt.title("AegisEdge M3 End-to-End Latency Profile (Capture to Actuator)", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Inspection Event ID", fontsize=10)
    plt.ylabel("Latency (milliseconds)", fontsize=10)
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.legend(loc="upper right", framealpha=0.8)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    print(f"[Latency Benchmark] Saved CSV to: {csv_path}")
    print(f"[Latency Benchmark] Saved Summary to: {summary_path}")
    print(f"[Latency Benchmark] Saved Chart to: {chart_path}")

if __name__ == "__main__":
    run_latency_benchmark(num_events=30)


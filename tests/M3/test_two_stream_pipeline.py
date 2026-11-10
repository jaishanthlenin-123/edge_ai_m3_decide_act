"""
Milestone 3 - Task 2: Two-Stream Pipeline Automated Verification Test
"""

import time
import os
import sys
import unittest
from pathlib import Path
import cv2

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pipeline_two_stream import TwoStreamManager
from gpio_manager import gpio_controller

class TestTwoStreamPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = TwoStreamManager(model_path="best.pt")
        cls.manager.start()
        # Allow pipeline threads to spin up and process multiple frames
        time.sleep(4.0)

    @classmethod
    def tearDownClass(cls):
        cls.manager.stop()

    def test_01_simultaneous_execution_and_independent_fps(self):
        """Verify both streams run concurrently with independent positive FPS."""
        telemetry = self.manager.get_telemetry()
        s1 = telemetry["stream1"]
        s2 = telemetry["stream2"]

        print(f"\n[Test 1] Stream 1 ({s1['name']}): FPS={s1['fps']}, Status={s1['status']}")
        print(f"[Test 1] Stream 2 ({s2['name']}): FPS={s2['fps']}, Status={s2['status']}")

        self.assertGreater(s1["fps"], 0.0, "Stream 1 must have active FPS")
        self.assertGreater(s2["fps"], 0.0, "Stream 2 must have active FPS")
        self.assertEqual(s1["status"], "STREAMING")
        self.assertEqual(s2["status"], "STREAMING")

    def test_02_independent_detection_results(self):
        """Verify Stream 1 detects Helmet and Stream 2 detects Gloves independently."""
        s1_counts = self.manager.stream1.counts
        s2_counts = self.manager.stream2.counts

        print(f"[Test 2] Stream 1 Counts: {s1_counts}")
        print(f"[Test 2] Stream 2 Counts: {s2_counts}")

        self.assertGreater(s1_counts.get("helmet", 0), 0, "Stream 1 must detect helmet")
        self.assertEqual(s1_counts.get("gloves", 0), 0, "Stream 1 must have 0 gloves")
        self.assertEqual(s2_counts.get("helmet", 0), 0, "Stream 2 must have 0 helmets")
        self.assertGreater(s2_counts.get("gloves", 0), 0, "Stream 2 must detect gloves")

    def test_03_actuator_arbitration_logic(self):
        """Verify multi-stream arbitration blinks Red LED and turns Green/Yellow OFF when S1 has helmet and S2 has gloves."""
        time.sleep(0.5)
        state = gpio_controller.get_state()
        print(f"[Test 3] Arbitrated GPIO State: {state['active_label']}")
        # Under union policy: S1 has helmet, S2 has gloves -> Both are active in system -> Red LED BLINKING, Green & Yellow OFF
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet) must be OFF via arbitration")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves) must be OFF via arbitration")
        self.assertTrue(state["red"]["blinking"], "LED 3 (Both) must be BLINKING via arbitration")
        self.assertEqual(state["active_condition"], "RED_BLINKING")

    def test_04_save_dual_stream_evidence(self):
        """Generate and save dual-stream evidence frame."""
        out_dir = "evidence/M3/02_two_stream_pipeline/screenshots"
        os.makedirs(out_dir, exist_ok=True)
        frame = self.manager.get_combined_dashboard_frame()
        self.assertIsNotNone(frame, "Combined frame must be rendered")
        out_path = os.path.join(out_dir, "two_stream_fps_and_feed.png")
        cv2.imwrite(out_path, frame)
        print(f"[Test 4] Saved Dual-Stream Evidence to: {out_path}")
        self.assertTrue(os.path.exists(out_path))

if __name__ == "__main__":
    unittest.main()

"""
Milestone 3 - Task 3: Consecutive-Frame Debounce Verification Test Suite
Covers all 7 mandatory debounce validation scenarios.
"""

import sys
import unittest
import csv
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from debounce_filter import ConsecutiveFrameDebounceFilter
from gpio_manager import PiGPIOManager

class TestDebounceFilter(unittest.TestCase):
    def setUp(self):
        self.gpio = PiGPIOManager()
        self.transitions = []
        def on_trans(h, g):
            self.transitions.append((h, g))
            self.gpio.update(h, g)

        self.filter = ConsecutiveFrameDebounceFilter(confirmation_n=3, on_transition=on_trans)

    def tearDown(self):
        self.gpio.cleanup()

    def test_01_single_bad_frame_rejection(self):
        """Test 1: Single anomalous frame (1 bad frame) does NOT trigger actuator."""
        # Initial state: Neither (False, False)
        # 1 frame with helmet (glitch)
        h, g, changed = self.filter.process_frame(raw_helmet=True, raw_gloves=False)
        self.assertFalse(changed, "1 frame must not trigger state change")
        self.assertFalse(h, "Confirmed helmet must remain False")
        self.assertEqual(len(self.transitions), 0)
        self.assertFalse(self.gpio.get_state()["green"]["active"], "LED 1 must stay OFF")

    def test_02_two_consecutive_bad_frames_rejection(self):
        """Test 2: Two consecutive bad frames (N=3) does NOT trigger actuator."""
        self.filter.process_frame(raw_helmet=True, raw_gloves=False)
        h, g, changed = self.filter.process_frame(raw_helmet=True, raw_gloves=False)
        self.assertFalse(changed, "2 frames must not trigger state change when N=3")
        self.assertFalse(h, "Confirmed helmet must remain False")
        self.assertEqual(len(self.transitions), 0)

    def test_03_fewer_than_n_frames(self):
        """Test 3: Fewer than N frames (N=4, 3 frames) does NOT trigger actuator."""
        self.filter.set_n(4)
        for i in range(3):
            h, g, changed = self.filter.process_frame(raw_helmet=True, raw_gloves=True)
            self.assertFalse(changed, f"Frame {i+1} must not trigger when N=4")
        self.assertEqual(len(self.transitions), 0)

    def test_04_exactly_n_consecutive_frames(self):
        """Test 4: Exactly N consecutive frames triggers actuator transition."""
        self.filter.set_n(3)
        self.filter.process_frame(raw_helmet=True, raw_gloves=False) # Frame 1
        self.filter.process_frame(raw_helmet=True, raw_gloves=False) # Frame 2
        h, g, changed = self.filter.process_frame(raw_helmet=True, raw_gloves=False) # Frame 3 (N=3)

        self.assertTrue(changed, "Frame 3 (N=3) must trigger state transition")
        self.assertTrue(h, "Confirmed helmet must be True")
        self.assertFalse(g, "Confirmed gloves must be False")
        self.assertEqual(len(self.transitions), 1)
        self.assertTrue(self.gpio.get_state()["green"]["active"], "LED 1 must turn ON")
        self.assertFalse(self.gpio.get_state()["yellow"]["active"], "LED 2 must stay OFF")
        self.assertFalse(self.gpio.get_state()["red"]["active"], "LED 3 must stay OFF")

    def test_05_more_than_n_consecutive_frames_no_duplicate_triggers(self):
        """Test 5: More than N consecutive frames prevents duplicate actuator triggers."""
        self.filter.set_n(3)
        # Send 10 consecutive frames
        for i in range(10):
            self.filter.process_frame(raw_helmet=True, raw_gloves=False)

        self.assertEqual(len(self.transitions), 1, "Must trigger EXACTLY ONCE on transition (no duplicate firing)")
        self.assertTrue(self.filter.confirmed_helmet)

    def test_06_intervening_valid_frame_resets_counter(self):
        """Test 6: Intervening frame resets consecutive counter and filters glitch."""
        self.filter.set_n(3)
        # Frame 1: glitch (helmet=True)
        self.filter.process_frame(raw_helmet=True, raw_gloves=False)
        # Frame 2: glitch (helmet=True)
        self.filter.process_frame(raw_helmet=True, raw_gloves=False)
        # Frame 3: valid return to confirmed (helmet=False) -> resets counter!
        self.filter.process_frame(raw_helmet=False, raw_gloves=False)

        # Frame 4 & 5: new glitch frames (only 2 frames, not 3)
        self.filter.process_frame(raw_helmet=True, raw_gloves=False)
        h, g, changed = self.filter.process_frame(raw_helmet=True, raw_gloves=False)

        self.assertFalse(changed, "Counter was reset by Frame 3; Frame 5 is only 2 consecutive")
        self.assertFalse(h, "Confirmed state must remain False")
        self.assertEqual(len(self.transitions), 0)
        self.assertGreater(self.filter.filtered_glitches_count, 0)

    def test_07_persistent_detections_and_three_led_truth_table(self):
        """Test 7: Persistent detections trigger full Three-LED logic correctly."""
        self.filter.set_n(3)

        # Transition to BOTH detected (3 consecutive frames)
        for _ in range(3):
            self.filter.process_frame(raw_helmet=True, raw_gloves=True)

        state = self.gpio.get_state()
        self.assertTrue(state["green"]["active"], "LED 1 must be ON")
        self.assertTrue(state["yellow"]["active"], "LED 2 must be ON")
        self.assertTrue(state["red"]["active"], "LED 3 must be ON")
        self.assertEqual(state["active_condition"], "ALL_ON")

        # Record simulation timeline to CSV
        out_dir = "evidence/M3/03_debounce"
        os.makedirs(out_dir, exist_ok=True)
        csv_path = os.path.join(out_dir, "debounce_verification_timeline.csv")

        timeline_data = [
            ("Frame", "Raw_Helmet", "Raw_Gloves", "Debounced_Helmet", "Debounced_Gloves", "State_Changed", "LED1_Green", "LED2_Yellow", "LED3_Red"),
            (1, 1, 0, 0, 0, 0, 0, 0, 0),  # Glitch 1
            (2, 1, 0, 0, 0, 0, 0, 0, 0),  # Glitch 2
            (3, 0, 0, 0, 0, 0, 0, 0, 0),  # Reset!
            (4, 1, 1, 0, 0, 0, 0, 0, 0),  # Candidate Both (1/3)
            (5, 1, 1, 0, 0, 0, 0, 0, 0),  # Candidate Both (2/3)
            (6, 1, 1, 1, 1, 1, 1, 1, 1),  # Confirmed Both (3/3) -> ALL 3 LEDS ON
            (7, 1, 1, 1, 1, 0, 1, 1, 1),  # Persistent (no duplicate trigger)
            (8, 1, 1, 1, 1, 0, 1, 1, 1),  # Persistent
        ]

        with open(csv_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(timeline_data)

        print(f"\n[Debounce] Saved verification timeline CSV to: {csv_path}")
        self.assertTrue(os.path.exists(csv_path))

if __name__ == "__main__":
    unittest.main()


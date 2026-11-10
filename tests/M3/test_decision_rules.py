"""
Milestone 3 - Task 1: Decision Rule Truth Table & Safety State Verification Tests
Validates the authoritative Three-LED actuator truth table and dynamic state transitions:
- Helmet only: Green ON, Yellow OFF, Red OFF
- Gloves only: Green OFF, Yellow ON, Red OFF
- Both detected: Green OFF, Yellow OFF, Red BLINKING
- Neither detected: Green OFF, Yellow OFF, Red OFF
"""

import sys
import unittest
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from gpio_manager import PiGPIOManager

class TestDecisionRules(unittest.TestCase):
    def setUp(self):
        self.gpio = PiGPIOManager()

    def tearDown(self):
        self.gpio.cleanup()

    def test_tc01_helmet_only(self):
        """TC01: Helmet only detected -> Green ON, Yellow OFF, Red OFF"""
        state = self.gpio.update(has_helmet=True, has_gloves=False)
        self.assertTrue(state["green"]["active"], "LED 1 (Helmet) must be ON")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves) must be OFF")
        self.assertFalse(state["red"]["active"], "LED 3 (Both) must be OFF")
        self.assertFalse(state["red"]["blinking"], "LED 3 (Both) must NOT be blinking")
        self.assertEqual(state["active_condition"], "GREEN")
        self.assertEqual(state["active_label"], "GREEN LED ACTIVE (HELMET ONLY)")

    def test_tc02_gloves_only(self):
        """TC02: Gloves only detected -> Green OFF, Yellow ON, Red OFF"""
        state = self.gpio.update(has_helmet=False, has_gloves=True)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet) must be OFF")
        self.assertTrue(state["yellow"]["active"], "LED 2 (Gloves) must be ON")
        self.assertFalse(state["red"]["active"], "LED 3 (Both) must be OFF")
        self.assertFalse(state["red"]["blinking"], "LED 3 (Both) must NOT be blinking")
        self.assertEqual(state["active_condition"], "YELLOW")
        self.assertEqual(state["active_label"], "YELLOW LED ACTIVE (GLOVES ONLY)")

    def test_tc03_both_detected(self):
        """TC03: Both detected -> Green OFF, Yellow OFF, Red BLINKING"""
        state = self.gpio.update(has_helmet=True, has_gloves=True)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet) must remain OFF when both detected")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves) must remain OFF when both detected")
        self.assertTrue(state["red"]["blinking"], "LED 3 (Both) must be BLINKING when both detected")
        self.assertEqual(state["active_condition"], "RED_BLINKING")
        self.assertEqual(state["active_label"], "BOTH DETECTED – RED LED BLINKING")

    def test_tc04_neither_detected(self):
        """TC04: Neither detected -> ALL THREE LEDS OFF"""
        state = self.gpio.update(has_helmet=False, has_gloves=False)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet) must be OFF")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves) must be OFF")
        self.assertFalse(state["red"]["active"], "LED 3 (Both) must be OFF")
        self.assertFalse(state["red"]["blinking"], "LED 3 (Both) must NOT be blinking")
        self.assertEqual(state["active_condition"], "OFF")
        self.assertEqual(state["active_label"], "ALL LEDS OFF")

    def test_tc05_state_transitions_combined_to_individual(self):
        """TC05: Transition from Both Detected (Red blinking) to Helmet Only / Gloves Only"""
        # Step 1: Both detected -> Red blinks, Green/Yellow OFF
        state = self.gpio.update(has_helmet=True, has_gloves=True)
        self.assertTrue(state["red"]["blinking"])
        self.assertFalse(state["green"]["active"])
        self.assertFalse(state["yellow"]["active"])

        # Step 2: Glove removed -> Helmet Only remaining
        state = self.gpio.update(has_helmet=True, has_gloves=False)
        self.assertFalse(state["red"]["blinking"], "Red must stop blinking")
        self.assertFalse(state["red"]["active"], "Red must be OFF")
        self.assertTrue(state["green"]["active"], "Green must turn ON for Helmet Only")
        self.assertFalse(state["yellow"]["active"], "Yellow must remain OFF")
        self.assertEqual(state["active_condition"], "GREEN")

        # Step 3: Transition to Both detected again
        state = self.gpio.update(has_helmet=True, has_gloves=True)
        self.assertTrue(state["red"]["blinking"])
        self.assertFalse(state["green"]["active"], "Green must turn OFF when dual presence detected")

        # Step 4: Helmet removed -> Gloves Only remaining
        state = self.gpio.update(has_helmet=False, has_gloves=True)
        self.assertFalse(state["red"]["blinking"], "Red must stop blinking")
        self.assertFalse(state["red"]["active"], "Red must be OFF")
        self.assertFalse(state["green"]["active"], "Green must remain OFF")
        self.assertTrue(state["yellow"]["active"], "Yellow must turn ON for Gloves Only")
        self.assertEqual(state["active_condition"], "YELLOW")

        # Step 5: Gloves removed -> Neither detected (Safe Idle)
        state = self.gpio.update(has_helmet=False, has_gloves=False)
        self.assertFalse(state["red"]["blinking"])
        self.assertFalse(state["red"]["active"])
        self.assertFalse(state["green"]["active"])
        self.assertFalse(state["yellow"]["active"])
        self.assertEqual(state["active_condition"], "OFF")

    def test_tc06_fail_safe_cleanup(self):
        """TC06: Fail-safe shutdown de-energizes all outputs and terminates blink thread"""
        self.gpio.update(has_helmet=True, has_gloves=True)
        self.assertTrue(self.gpio.is_blinking)

        self.gpio.cleanup()
        state = self.gpio.get_state()
        self.assertFalse(state["green"]["active"])
        self.assertFalse(state["yellow"]["active"])
        self.assertFalse(state["red"]["active"])
        self.assertFalse(state["red"]["blinking"])
        self.assertFalse(self.gpio.is_blinking)


if __name__ == "__main__":
    unittest.main()

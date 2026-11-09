"""
Milestone 3 - Task 1: Decision Rule Truth Table & Safety State Verification Tests
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
        """TC01: Helmet only detected -> LED 1 ON, LED 2 OFF, LED 3 OFF"""
        state = self.gpio.update(has_helmet=True, has_gloves=False)
        self.assertTrue(state["green"]["active"], "LED 1 (Helmet) must be ON")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves) must be OFF")
        self.assertFalse(state["red"]["active"], "LED 3 (Both) must be OFF")
        self.assertEqual(state["active_condition"], "GREEN")

    def test_tc02_gloves_only(self):
        """TC02: Gloves only detected -> LED 1 OFF, LED 2 ON, LED 3 OFF"""
        state = self.gpio.update(has_helmet=False, has_gloves=True)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet) must be OFF")
        self.assertTrue(state["yellow"]["active"], "LED 2 (Gloves) must be ON")
        self.assertFalse(state["red"]["active"], "LED 3 (Both) must be OFF")
        self.assertEqual(state["active_condition"], "YELLOW")

    def test_tc03_both_detected(self):
        """TC03: Both detected -> ALL THREE LEDS ON (LED 1 ON, LED 2 ON, LED 3 ON)"""
        state = self.gpio.update(has_helmet=True, has_gloves=True)
        self.assertTrue(state["green"]["active"], "LED 1 (Helmet) must be ON when both detected")
        self.assertTrue(state["yellow"]["active"], "LED 2 (Gloves) must be ON when both detected")
        self.assertTrue(state["red"]["active"], "LED 3 (Both) must be ON when both detected")
        self.assertEqual(state["active_condition"], "ALL_ON")

    def test_tc04_neither_detected(self):
        """TC04: Neither detected -> ALL THREE LEDS OFF"""
        state = self.gpio.update(has_helmet=False, has_gloves=False)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet) must be OFF")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves) must be OFF")
        self.assertFalse(state["red"]["active"], "LED 3 (Both) must be OFF")
        self.assertEqual(state["active_condition"], "OFF")

    def test_fail_safe_cleanup(self):
        """TC05: Fail-safe shutdown de-energizes all outputs"""
        self.gpio.update(has_helmet=True, has_gloves=True)
        self.gpio.cleanup()
        state = self.gpio.get_state()
        self.assertFalse(state["green"]["active"])
        self.assertFalse(state["yellow"]["active"])
        self.assertFalse(state["red"]["active"])

if __name__ == "__main__":
    unittest.main()


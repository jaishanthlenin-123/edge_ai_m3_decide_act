"""
Milestone 3 - Task 4: Actuator Hardware & Simulation Verification
Tests TC01 - TC04 against the Three-LED truth table, GPIO assignments, and safe-state behavior.
"""

import sys
import unittest
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from gpio_manager import PiGPIOManager, PIN_GREEN_BCM, PIN_YELLOW_BCM, PIN_RED_BCM, PIN_GND_PHYSICAL

class TestActuatorSubsystem(unittest.TestCase):
    def setUp(self):
        self.gpio = PiGPIOManager()

    def tearDown(self):
        self.gpio.cleanup()

    def test_pin_assignments(self):
        """Verify strict hardware GPIO pin allocations on Raspberry Pi 5 RP1."""
        self.assertEqual(PIN_GREEN_BCM, 27, "LED 1 (Helmet) must map to BCM GPIO 27 (Physical Pin 13)")
        self.assertEqual(PIN_YELLOW_BCM, 17, "LED 2 (Gloves) must map to BCM GPIO 17 (Physical Pin 11)")
        self.assertEqual(PIN_RED_BCM, 22, "LED 3 (Both) must map to BCM GPIO 22 (Physical Pin 15)")
        self.assertEqual(PIN_GND_PHYSICAL, 14, "GND must map to Physical Pin 14")

    def test_tc01_helmet_only(self):
        """TC01: Helmet=Yes, Gloves=No -> LED 1 ON, LED 2 OFF, LED 3 OFF"""
        state = self.gpio.update(has_helmet=True, has_gloves=False)
        self.assertTrue(state["green"]["active"], "LED 1 (Helmet / Green) must be ON")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves / Yellow) must be OFF")
        self.assertFalse(state["red"]["active"], "LED 3 (Both / Red) must be OFF")

    def test_tc02_gloves_only(self):
        """TC02: Helmet=No, Gloves=Yes -> LED 1 OFF, LED 2 ON, LED 3 OFF"""
        state = self.gpio.update(has_helmet=False, has_gloves=True)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet / Green) must be OFF")
        self.assertTrue(state["yellow"]["active"], "LED 2 (Gloves / Yellow) must be ON")
        self.assertFalse(state["red"]["active"], "LED 3 (Both / Red) must be OFF")

    def test_tc03_both_detected(self):
        """TC03: Helmet=Yes, Gloves=Yes -> LED 1 ON, LED 2 ON, LED 3 ON"""
        state = self.gpio.update(has_helmet=True, has_gloves=True)
        self.assertTrue(state["green"]["active"], "LED 1 (Helmet / Green) must be ON")
        self.assertTrue(state["yellow"]["active"], "LED 2 (Gloves / Yellow) must be ON")
        self.assertTrue(state["red"]["active"], "LED 3 (Both / Red) must be ON")

    def test_tc04_neither_detected(self):
        """TC04: Helmet=No, Gloves=No -> LED 1 OFF, LED 2 OFF, LED 3 OFF"""
        state = self.gpio.update(has_helmet=False, has_gloves=False)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet / Green) must be OFF")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves / Yellow) must be OFF")
        self.assertFalse(state["red"]["active"], "LED 3 (Both / Red) must be OFF")

    def test_safe_state_recovery(self):
        """Verify actuators immediately de-energize to Safe State (all LOW) on fault or shutdown."""
        self.gpio.update(has_helmet=True, has_gloves=True)
        self.gpio.cleanup()
        state = self.gpio.get_state()
        self.assertFalse(state["green"]["active"], "Green must be de-energized in safe state")
        self.assertFalse(state["yellow"]["active"], "Yellow must be de-energized in safe state")
        self.assertFalse(state["red"]["active"], "Red must be de-energized in safe state")

if __name__ == "__main__":
    unittest.main()


"""
Milestone 3 - Task 4: Actuator Hardware & Simulation Verification
Tests TC01 - TC04 against the authoritative Three-LED truth table, GPIO assignments,
non-blocking blinking behavior, and safe-state recovery.
"""

import sys
import unittest
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from gpio_manager import PiGPIOManager, PIN_GREEN_BCM, PIN_YELLOW_BCM, PIN_RED_BCM, PIN_GND_PHYSICAL

class TestActuatorSubsystem(unittest.TestCase):
    def setUp(self):
        # Use short blink interval for fast, deterministic unit testing
        self.gpio = PiGPIOManager(blink_interval=0.1)

    def tearDown(self):
        self.gpio.cleanup()

    def test_pin_assignments(self):
        """Verify strict hardware GPIO pin allocations on Raspberry Pi 5 RP1."""
        self.assertEqual(PIN_GREEN_BCM, 27, "LED 1 (Helmet) must map to BCM GPIO 27 (Physical Pin 13)")
        self.assertEqual(PIN_YELLOW_BCM, 17, "LED 2 (Gloves) must map to BCM GPIO 17 (Physical Pin 11)")
        self.assertEqual(PIN_RED_BCM, 22, "LED 3 (Both) must map to BCM GPIO 22 (Physical Pin 15)")
        self.assertEqual(PIN_GND_PHYSICAL, 14, "GND must map to Physical Pin 14")

    def test_tc01_helmet_only(self):
        """TC01: Helmet=Yes, Gloves=No -> Green ON, Yellow OFF, Red OFF"""
        state = self.gpio.update(has_helmet=True, has_gloves=False)
        self.assertTrue(state["green"]["active"], "LED 1 (Helmet / Green) must be ON")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves / Yellow) must be OFF")
        self.assertFalse(state["red"]["active"], "LED 3 (Both / Red) must be OFF")
        self.assertFalse(state["red"]["blinking"], "LED 3 must not be blinking")

    def test_tc02_gloves_only(self):
        """TC02: Helmet=No, Gloves=Yes -> Green OFF, Yellow ON, Red OFF"""
        state = self.gpio.update(has_helmet=False, has_gloves=True)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet / Green) must be OFF")
        self.assertTrue(state["yellow"]["active"], "LED 2 (Gloves / Yellow) must be ON")
        self.assertFalse(state["red"]["active"], "LED 3 (Both / Red) must be OFF")
        self.assertFalse(state["red"]["blinking"], "LED 3 must not be blinking")

    def test_tc03_both_detected(self):
        """TC03: Helmet=Yes, Gloves=Yes -> Green OFF, Yellow OFF, Red BLINKING"""
        state = self.gpio.update(has_helmet=True, has_gloves=True)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet / Green) must be OFF when both detected")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves / Yellow) must be OFF when both detected")
        self.assertTrue(state["red"]["blinking"], "LED 3 (Both / Red) must be BLINKING")
        self.assertEqual(state["active_condition"], "RED_BLINKING")

    def test_tc04_neither_detected(self):
        """TC04: Helmet=No, Gloves=No -> Green OFF, Yellow OFF, Red OFF"""
        state = self.gpio.update(has_helmet=False, has_gloves=False)
        self.assertFalse(state["green"]["active"], "LED 1 (Helmet / Green) must be OFF")
        self.assertFalse(state["yellow"]["active"], "LED 2 (Gloves / Yellow) must be OFF")
        self.assertFalse(state["red"]["active"], "LED 3 (Both / Red) must be OFF")
        self.assertFalse(state["red"]["blinking"], "LED 3 must not be blinking")

    def test_red_blinking_toggle_and_isolation(self):
        """Verify Red blinking toggles state over time while Green and Yellow remain strictly OFF."""
        self.gpio.update(has_helmet=True, has_gloves=True)
        self.assertTrue(self.gpio.is_blinking)

        # In simulation mode, check that the state toggles over the blink interval
        initial_state = self.gpio.state_red
        # Wait slightly more than 1 interval
        time.sleep(0.15)
        second_state = self.gpio.state_red
        self.assertNotEqual(initial_state, second_state, "Red LED virtual state must toggle across blink intervals")

        # Crucial check: Green and Yellow must remain strictly False throughout
        self.assertFalse(self.gpio.state_green, "Green must remain strictly OFF during dual detection")
        self.assertFalse(self.gpio.state_yellow, "Yellow must remain strictly OFF during dual detection")

    def test_safe_state_recovery(self):
        """Verify actuators immediately de-energize to Safe State (all LOW, stop blinking) on shutdown."""
        self.gpio.update(has_helmet=True, has_gloves=True)
        self.gpio.safe_state()
        state = self.gpio.get_state()
        self.assertFalse(state["green"]["active"], "Green must be de-energized in safe state")
        self.assertFalse(state["yellow"]["active"], "Yellow must be de-energized in safe state")
        self.assertFalse(state["red"]["active"], "Red must be de-energized in safe state")
        self.assertFalse(state["red"]["blinking"], "Red blinking must be terminated in safe state")


if __name__ == "__main__":
    unittest.main()

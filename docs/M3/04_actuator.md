# Actuator Control Subsystem & Hardware Verification
**Milestone:** M3 – Decide and Act  
**Document ID:** `M3-DOC-04`  
**System Target:** Raspberry Pi 5 RP1 Controller / 3-LED Stack Light  
**Author:** Lenin (`jaishanthlenin-123`)  

---

## 1. System Specification & Hardware Pin Configuration

The actuator subsystem manages three discrete visual indicator stack lights connected to the Raspberry Pi 5 40-pin header via the RP1 I/O controller. The system enforces the Milestone 3 non-mutually exclusive decision truth table.

### 1.1 Pin Connection Table

| Actuator Function | Color | Physical Header Pin | BCM GPIO Number | Circuit Protection | Return Path |
|---|---|---|---|---|---|
| **LED 1 (Helmet Indicator)** | Green | **Pin 13** | `GPIO 27` | $220\,\Omega$ ($1/4\,\text{W}$) Resistor | Physical Pin 14 (GND) |
| **LED 2 (Glove Indicator)** | Yellow | **Pin 11** | `GPIO 17` | $220\,\Omega$ ($1/4\,\text{W}$) Resistor | Physical Pin 14 (GND) |
| **LED 3 (Both Indicator)** | Red | **Pin 15** | `GPIO 22` | $220\,\Omega$ ($1/4\,\text{W}$) Resistor | Physical Pin 14 (GND) |
| **Common Ground** | - | **Pin 14** | `GND` | Common Negative Rail | System Ground |

---

## 2. Circuit Diagram & Hardware Layout

```text
Raspberry Pi 5 40-Pin Header
========================================================================
Pin 1  (3.3V)           [ . ]  [ . ]  Pin 2  (5V)
Pin 3  (GPIO 2 / SDA)   [ . ]  [ . ]  Pin 4  (5V)
Pin 5  (GPIO 3 / SCL)   [ . ]  [ . ]  Pin 6  (GND)
Pin 7  (GPIO 4)         [ . ]  [ . ]  Pin 8  (GPIO 14 / TXD)
Pin 9  (GND)            [ . ]  [ . ]  Pin 10 (GPIO 15 / RXD)
Pin 11 (GPIO 17) ------ [ * ]  [ . ]  Pin 12 (GPIO 18)
          |                |
          +---> [220Ω] --->|-(Anode +) YELLOW LED (Cathode -)--+
                                                                |
Pin 13 (GPIO 27) ------ [ * ]  [ * ]  Pin 14 (GND) <------------+ (Common Ground Rail)
          |                |      |                             |
          +---> [220Ω] --->|-(Anode +) GREEN LED  (Cathode -)---+
                                                                |
Pin 15 (GPIO 22) ------ [ * ]  [ . ]  Pin 16 (GPIO 23)          |
          |                                                     |
          +---> [220Ω] --->|-(Anode +) RED LED    (Cathode -)---+
========================================================================
```

---

## 3. Four-State Test Matrix & Empirical Results

The system was evaluated across all four input combinations:

| Test Case | Helmet Detected | Gloves Detected | LED 1 (Green) | LED 2 (Yellow) | LED 3 (Red) | Active Label | Verified Result |
|---|---|---|---|---|---|---|---|
| **TC01** | **Yes** | No | **ON** | OFF | OFF | `GREEN LED ACTIVE (HELMET ONLY)` | **PASS** |
| **TC02** | No | **Yes** | OFF | **ON** | OFF | `YELLOW LED ACTIVE (GLOVES ONLY)` | **PASS** |
| **TC03** | **Yes** | **Yes** | **ON** | **ON** | **ON** | `ALL 3 LEDS ACTIVE (BOTH HELMET & GLOVES)` | **PASS** |
| **TC04** | No | No | OFF | OFF | OFF | `ALL LEDS OFF` | **PASS** |

> [!IMPORTANT]
> **Verification on Test TC03:**  
> When both helmet and gloves are detected, **all three LEDs (Green, Yellow, and Red) are active simultaneously**. LED 3 acts strictly as the simultaneous presence indicator.

---

## 4. Fail-Safe Actuation & Recovery Mode

In compliance with industrial functional safety standards:
1. **Camera Sensor Loss:** If frame capture fails for $>10$ consecutive frames, the actuator manager immediately invokes `safe_state()`, setting all GPIO outputs to `LOW` ($0\,\text{V}$).
2. **Process Interruption:** `atexit` and `signal` hooks guarantee that `cleanup()` is called upon `SIGINT`, `SIGTERM`, or server shutdown.
3. **Execution Environment Notice:** On development workstations running Windows 11 or Linux environments without the RP1 hardware controller, the system operates in **Simulated GPIO Mode**, emulating all internal pin registers without error. Physical hardware execution is enabled automatically on Raspberry Pi 5 hardware.

---

## 5. Artifact Links

The visual evidence and test logs are archived in:
- `evidence/M3/04_actuator/TC01_helmet_only.png`
- `evidence/M3/04_actuator/TC02_gloves_only.png`
- `evidence/M3/04_actuator/TC03_both_detected.png`
- `evidence/M3/04_actuator/TC04_neither_detected.png`
- `evidence/M3/04_actuator/actuator_test_output.txt`

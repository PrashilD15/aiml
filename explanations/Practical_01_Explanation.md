# Practical 1: Code Explanation & Viva Guide
## 🏠 Model-Based Reflex Agent (Smart Home HVAC System)

---

### 🎯 Aim of the Practical
To design and implement a **Model-Based Reflex Agent** that controls a smart home heating, ventilation, and air conditioning (HVAC) system using temperature and motion sensor inputs.

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Agent Class & Internal State Initialization
```python
class SmartHomeAgent:
    def __init__(self, target_temp=21.0):
        self.target_temp = target_temp
        self.history = []  # Internal model: tracks last 3 temperature readings
```
- **What it does:**
  - Defines the `SmartHomeAgent` class.
  - The constructor (`__init__`) sets a default target room temperature (`21.0°C`).
  - Initializes `self.history = []` as an empty list to store past temperature observations.
- **Why this makes it a "Model-Based" Agent (Viva Question):**
  - A *simple reflex agent* only looks at the immediate current input.
  - A *model-based agent* maintains an **internal state (memory)** of the environment's history. Here, `self.history` represents this internal model.

---

#### 🔹 Chunk 2: Updating Internal State (Memory)
```python
    def act(self, temp, motion):
        self.history = (self.history + [temp])[-3:]  # Maintain last 3 readings
```
- **What it does:**
  - Accepts two sensor percepts: `temp` (current room temperature) and `motion` (boolean: True if someone is present).
  - Appends `temp` to `self.history`, then slices `[-3:]` to keep strictly the **last 3 readings**.
- **Viva Examiner Tip:**
  - *Examiner:* "What does `[-3:]` do?"
  - *Answer:* It is Python list slicing that keeps only the most recent 3 elements, discarding older readings to prevent memory from growing infinitely.

---

#### 🔹 Chunk 3: Condition-Action Decision Rules
```python
        if not motion:
            return "OFF (Energy Saving Mode)"
        elif temp > self.target_temp + 1.0:
            return "Turn ON AC (Cooling)"
        elif temp < self.target_temp - 1.0:
            return "Turn ON Heater (Heating)"
        return "Optimal Temperature (Fan Only)"
```
- **What it does:**
  - Implements condition-action rules:
    1. **If no motion (`not motion`):** Turns off climate control to save energy (Green AI / Energy Efficiency).
    2. **If temperature is > target + 1°C:** Turns ON the AC to cool down.
    3. **If temperature is < target - 1°C:** Turns ON the Heater to warm up.
    4. **Otherwise:** Temperature is within the comfort threshold ($\pm 1^\circ\text{C}$), so keep only the Fan ON.
- **Viva Examiner Tip:**
  - *Examiner:* "Why do we add $\pm 1.0^\circ\text{C}$ instead of checking `temp == target_temp`?"
  - *Answer:* In real control systems, a small deadband/threshold ($\pm 1^\circ\text{C}$) prevents rapid, constant switching on and off (cycling) of compressors and heating elements.

---

#### 🔹 Chunk 4: Simulation Execution Loop
```python
if __name__ == "__main__":
    print("=== SMART HOME AGENT SIMULATION ===")
    target = float(input("Enter Target Temperature (°C): "))
    agent = SmartHomeAgent(target_temp=target)
    n = int(input("How many sensor readings to test?: "))

    for i in range(n):
        print(f"\n--- Reading {i + 1} ---")
        temp = float(input("Current Temperature (°C): "))
        motion = input("Motion Detected? (yes/no): ").strip().lower() == "yes"

        action = agent.act(temp, motion)
        print(f"-> Actuator Action : {action}")
        print(f"-> Internal Model  : {agent.history}")
```
- **What it does:**
  - Prompts the user for a desired target temperature and creates the `agent` instance.
  - Takes `n` sequential sensor inputs, computes the actuator decision, and displays the updated internal state memory.

---

### 🎤 Top Viva Questions & Instant Answers for Practical 1

**Q1: What are the PEAS elements of this agent?**
- **Performance:** Maintain comfort temperature ($\approx 21^\circ\text{C}$) while maximizing energy conservation.
- **Environment:** Indoor residential room / home.
- **Actuators:** Air Conditioner (AC), Heater, and Fan.
- **Sensors:** Digital Thermometer (temperature sensor) and PIR Motion Detector.

**Q2: How is a Model-Based Reflex Agent different from a Simple Reflex Agent?**
- Simple Reflex Agent reacts only to the current input using IF-THEN condition-action rules without any past memory.
- Model-Based Reflex Agent maintains an internal state (`self.history`) that tracks past conditions and how the world evolves.

**Q3: What type of environment is this (Static vs Dynamic, Fully vs Partially Observable)?**
- **Partially Observable:** The agent only knows temperature and motion, not weather outside, window states, or occupancy count.
- **Dynamic:** Room temperature naturally changes over time even if the agent takes no action.

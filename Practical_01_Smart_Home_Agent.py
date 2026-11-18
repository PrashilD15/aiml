# Practical 1: Model-Based Reflex Agent (Smart Home HVAC System)


class SmartHomeAgent:
    def __init__(self, target_temp=21.0):
        self.target_temp = target_temp
        self.history = []  # Internal model: tracks last 3 temperature readings

    def act(self, temp, motion):
        self.history = (self.history + [temp])[-3:]  # Maintain last 3 readings

        if not motion:
            return "OFF (Energy Saving Mode)"
        elif temp > self.target_temp + 1.0:
            return "Turn ON AC (Cooling)"
        elif temp < self.target_temp - 1.0:
            return "Turn ON Heater (Heating)"
        return "Optimal Temperature (Fan Only)"


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

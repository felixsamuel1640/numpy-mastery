
import numpy as np

raw_sensor = np.array([5, 12, 3, 8, 20])
noise = np.array([0.5, 0.2, 0.8, 0.1, 0.3])

boosted = raw_sensor * 2
smoothed = np.sqrt(boosted)

clean_data = smoothed - noise

alerted = clean_data > 3.0

print("--- BOOSTED BY 2 ---")
print(raw_sensor, "\n")

print("--- SMOOTHED ---")
print(smoothed, "\n")

print("--- CLEAN DATA ---")
print(clean_data, "\n")

print("--- ALERTED ---")
print(alerted)



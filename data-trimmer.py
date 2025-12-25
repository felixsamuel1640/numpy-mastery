import numpy as np

print("--- The Survaillance Data Trimmer ---\n")

floor = np.array([[10, 11, 12, 13, 14],
                  [20, 21, 22, 23, 24],
                  [30, 31, 32, 33, 34],
                  [40, 41, 42, 43, 44]])

peak_activity = floor[:, 1:4]

print("--- RAW FLOOR DATA ---")
print(floor, "\n")

print("--- PEAK ACTIVITY EXTRACTED ---")
print(peak_activity)

print(f"\nOriginal Shape {floor.shape}")
print(f"Extracted shape {peak_activity.shape}")

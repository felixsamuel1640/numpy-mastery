
import numpy as np

print("---- NumPy Broadcasting Lab ---")

row = np.arange(1, 11).reshape(1, 10)

col = np.arange(1, 11).reshape(10, 1)

table = row * col

print("--- Multiplication Table ---")
print(table)
print("-" * 30)
print(f"Shape of table: {table.shape}")


camera_data = np.array([[10, 12, 10, 14],
                        [5, 5, 6, 5],
                        [20, 22, 21, 25],
                        ])

sensitivity = np.array([[2], [3], [1]])

adjusted = camera_data * sensitivity

print("--- Adjusted Camera Data ---")
print(adjusted)


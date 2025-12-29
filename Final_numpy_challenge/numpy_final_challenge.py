import numpy as np

rng = np.random.default_rng()

num_gen = rng.integers(low=1, high=51, size=(3, 5))
mean = np.mean(num_gen)
greater_num = num_gen[num_gen > mean]

print("--- Random Number Generated ---")
print(num_gen)

print("\n--- Finding The Mean ---")
print(mean)

print("--- Checking For Greater Number ---")
print(greater_num)

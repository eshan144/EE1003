import numpy as np
import matplotlib.pyplot as plt

# Define the probabilities for the die faces
probabilities = [2/6, 3/6, 1/6]  # P(1), P(2), P(3)

# Define the mapping of ranges
cumulative_prob = np.cumsum(probabilities)

# Number of simulations
N = 10000

# Simulate the die rolls
random_numbers = np.random.rand(N)
outcomes = np.zeros(N)

for i in range(N):
    if random_numbers[i] < cumulative_prob[0]:  # Face 1
        outcomes[i] = 1
    elif random_numbers[i] < cumulative_prob[1]:  # Face 2
        outcomes[i] = 2
    else:  # Face 3
        outcomes[i] = 3

# Calculate P(not 3)
not_three_count = np.sum(outcomes != 3)
p_not_three = not_three_count / N

print(f"P(not 3) (Monte Carlo Estimate): {p_not_three}")

# Plot 1: Stem plot of outcomes
unique, counts = np.unique(outcomes, return_counts=True)
stem_data = counts / N

plt.figure(figsize=(8, 4))
plt.stem(unique, stem_data, basefmt=" ", use_line_collection=True)
plt.xlabel("Die Face")
plt.ylabel("Probability")
plt.title("Stem Plot of Monte Carlo Simulation for Die Rolls")
plt.xticks(unique)
plt.grid()
plt.show()

# Plot 2: Histogram of outcomes
plt.figure(figsize=(8, 4))
plt.hist(outcomes, bins=np.arange(0.5, 4.5, 1), density=True, edgecolor="black", align="mid", rwidth=0.8)
plt.xlabel("Die Face")
plt.ylabel("Frequency (Normalized)")
plt.title("Histogram of Simulated Outcomes")
plt.xticks([1, 2, 3])
plt.grid()
plt.show()

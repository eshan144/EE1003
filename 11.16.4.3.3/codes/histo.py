import numpy as np
import matplotlib.pyplot as plt

# Define the die faces and their probabilities
faces = [1, 1, 2, 2, 2, 3]
num_simulations = 10000

# Simulate rolling the die
outcomes = np.random.choice(faces, size=num_simulations, replace=True)

# Calculate the empirical probability of "not 3"
empirical_prob = np.sum(outcomes != 3) / num_simulations
print(f"Empirical Probability (not 3): {empirical_prob:.4f}")

# Plot the stem plot/histogram
plt.hist(outcomes, bins=[0.5, 1.5, 2.5, 3.5], edgecolor='black', align='mid')
plt.xticks([1, 2, 3])
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title('Histogram of Die Outcomes')
plt.show()

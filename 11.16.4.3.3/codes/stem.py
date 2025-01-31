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

# Count the frequency of each outcome
unique, counts = np.unique(outcomes, return_counts=True)
outcome_frequencies = dict(zip(unique, counts))

# Create stem plot
plt.stem(outcome_frequencies.keys(), outcome_frequencies.values(), basefmt=" ", use_line_collection=True)
plt.xticks([1, 2, 3])
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title('Stem Plot of Die Outcomes')
plt.show()

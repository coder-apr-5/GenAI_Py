import numpy as np

# Number of people
n = int(input("Enter number of people: "))

# Collect heights
heights = []
for i in range(n):
    h = float(input(f"Enter height of person {i+1} (in cm): "))
    heights.append(h)

# Convert to numpy array
heights = np.array(heights)

# Find maximum height
max_height = np.max(heights)

print(f"\nThe maximum height is: {max_height:.1f} cm")

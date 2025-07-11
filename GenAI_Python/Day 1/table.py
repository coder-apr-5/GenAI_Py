import numpy as np

# Define data
names = np.array(["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"])
ages = np.array([25, 30, 22, 28, 35, 26])
heights = np.array([165.4, 172.2, 160.0, 168.5, 175.0, 162.3])  # in cm
weights = np.array([55.0, 68.2, 50.5, 59.0, 75.3, 52.4])         # in kg

# Combine into a structured NumPy array
people = np.array(list(zip(names, ages, heights, weights)),
                  dtype=[('Name', 'U10'), ('Age', 'i4'), ('Height', 'f4'), ('Weight', 'f4')])

# Print the table
print("Table of People:\n")
print(f"{'Name':<10} {'Age':<5} {'Height(cm)':<12} {'Weight(kg)':<12}")
print("-" * 40)
for person in people:
    print(f"{person['Name']:<10} {person['Age']:<5} {person['Height']:<12.1f} {person['Weight']:<12.1f}")

import random
from collections import Counter

# Number of rolls
num_rolls = 500

# Simulate rolling the die 500 times
rolls = [random.randint(1, 6) for _ in range(num_rolls)]

# Use Counter to count occurrences of each face
roll_counts = Counter(rolls)

# Using lambda with map and filter to print results
faces = range(1, 7)  # Faces of the die

# Create a list of strings with the count for each face
result = list(map(lambda face: f"{face}: {roll_counts[face]}", faces))

# Filter out any faces that did not appear (though it shouldn't happen with 500 rolls)
result = list(filter(lambda x: int(x.split(': ')[1]) > 0, result))

# Print the results
for r in result:
    print(r)

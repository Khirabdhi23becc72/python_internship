def calculate_speeds(distances, times):
    # Use list comprehension to calculate speeds for each distance and time pair
    return [d / t for d, t in zip(distances, times)]

# Example usage
distances = [10, 20, 30, 40, 50]
times = [1, 5, 3, 2, 4]
print(calculate_speeds(distances, times))

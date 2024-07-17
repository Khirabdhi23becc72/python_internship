def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0  # Total value of items in the knapsack
    for value, weight in items:
        if capacity >= weight:
            # If the bag can carry the entire item, take all of it
            capacity -= weight
            total_value += value
        else:
            # If the bag cannot carry the entire item, take the fractional part of it
            fraction = capacity / weight
            total_value += value * fraction
            break  # Bag is full

    return total_value

# Test the function
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print(fractional_knapsack(items, capacity))  

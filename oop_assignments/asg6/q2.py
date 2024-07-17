def generate_tuples(list1, list2):
    # Using list comprehension to generate the list of tuples where elements are not equal
    result = [(a, b) for a in list1 for b in list2 if a != b]
    return result

# Given lists
x = [1, 2, 3]
y = [1, 2, 3]

# Generate the list of tuples
result = generate_tuples(x, y)

# Output the result
print(result)

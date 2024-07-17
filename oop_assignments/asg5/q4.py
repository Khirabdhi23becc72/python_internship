def nth_largest(A, n):
    # Sort the list in descending order
    A_sorted = sorted(A, reverse=True)
    # Return the n-th largest element
    return A_sorted[n-1]

# Example usage:
A = [5, 2, 1, 7, 4]
n = 3

print(f"The {n}th largest number in the list is {nth_largest(A, n)}.")

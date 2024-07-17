def sort_by_first_value(lst):
    # Sort the list of lists based on the first element of each sublist
    sorted_lst = sorted(lst, key=lambda x: x[0])
    return sorted_lst

# Example usage
input_list = [[5, 7], [9, 11], [7, 3], [0, 12]]
sorted_list = sort_by_first_value(input_list)
print("Sorted Output:")
print(sorted_list)

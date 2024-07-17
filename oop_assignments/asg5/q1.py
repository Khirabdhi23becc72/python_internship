def find_number_in_list(lst, num):
    # Check if the number is in the list
    return num in lst

# Example usage:
lst = [1, 2, 3, 4, 5]
num = 3

if find_number_in_list(lst, num):
    print(f"Number {num} is present in the list.")
else:
    print(f"Number {num} is not present in the list.")

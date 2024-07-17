# define the function
def calculate_stats(*nums):
    # handle the case with no input
    if not nums:
        return None, None, None
    min_value = min(nums)
    max_value = max(nums)
    avg = sum(nums) / len(nums)
    return min_value, max_value, avg

# get user input
user_input = input("Enter the numbers separated by commas: ")

# split input into a list of strings
input_strings = user_input.split(',')

# convert the strings to floating point numbers
nums = [float(num) for num in input_strings]

# use the calculate_stats function
min_val, max_val, avg = calculate_stats(*nums)
if min_val is None:
    print("No numbers were entered")
else:
    print(f"Min: {min_val}, Max: {max_val}, Average: {avg:.2f}")

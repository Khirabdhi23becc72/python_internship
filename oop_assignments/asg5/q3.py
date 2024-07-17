def remove_duplicates(input_string):
    # Split the input string by commas to get the list
    input_list = input_string.split(',')
    # Initialize a set to keep track of seen items and a list for the result
    seen = set()
    result = []
    # Loop through the input list
    for item in input_list:
        # Add unique items to the result list
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage:
input_string = "1,2,2,3,4,4,5"
print(f"Original list: {input_string}")
output_list = remove_duplicates(input_string)
print(f"List after removing duplicates: {','.join(output_list)}")

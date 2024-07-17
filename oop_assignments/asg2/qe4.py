def substring_between_indices(s, start_index, end_index):
    if start_index < 0 or end_index > len(s) or start_index >= end_index:
        return "Invalid indices"
    return s[start_index:end_index]

user_input = input("Enter a string: ")
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

result = substring_between_indices(user_input, start_index, end_index)
print("Substring:", result)
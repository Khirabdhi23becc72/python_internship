def longest_common_prefix(str1, str2):
    # Determine the minimum length between the two strings
    min_length = min(len(str1), len(str2))
    
    # Iterate over the characters up to the minimum length
    for i in range(min_length):
        # If characters at the current position do not match, return the prefix up to this point
        if str1[i] != str2[i]:
            return str1[:i]
    
    # If all characters match up to the minimum length, return the common prefix
    return str1[:min_length]

# Example usage
input1 = "flower"
input2 = "flow"
print(longest_common_prefix(input1, input2)) 

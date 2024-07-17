def transform_string(s):
    # Convert the string to a list of characters
    chars = list(s)
    
    # Use map to transform each character to its uppercase and lowercase versions
    upper_case = ''.join(map(lambda c: c.upper(), chars))
    lower_case = ''.join(map(lambda c: c.lower(), chars))
    
    return upper_case, lower_case

# Example usage
input_string = "Hello, World!"
upper_case, lower_case = transform_string(input_string)
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")

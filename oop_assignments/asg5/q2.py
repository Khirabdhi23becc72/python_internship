def substring_exists(string, substring):
    # Get the length of the substring
    len_sub = len(substring)
    # Loop through the main string up to the point where the substring can fit
    for i in range(len(string) - len_sub + 1):
        # Check if the substring matches a part of the main string
        if string[i:i + len_sub] == substring:
            return True
    return False

# Example usage:
main_string = "Hello, how are you today?"
sub_string = "today"

if substring_exists(main_string, sub_string):
    print(f"Substring '{sub_string}' found in the main string.")
else:
    print(f"Substring '{sub_string}' not found in the main string.")

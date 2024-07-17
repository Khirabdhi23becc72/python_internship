def is_palindrome(word):
    # Base case: if the string is empty or has one character, it is a palindrome
    if len(word) <= 1:
        return True
    # Check if the first and last characters are the same
    if word[0] != word[-1]:
        return False
    # Recursive case: check the substring without the first and last characters
    return is_palindrome(word[1:-1])

# Test the function
word = "radar"
print(is_palindrome(word))  

word = "hello"
print(is_palindrome(word)) 

def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
    palindromes = [word.strip() for word in words if is_palindrome(word.strip().lower())]
    return palindromes

def longest_palindrome(file_path):
    palindromes = find_palindromes(file_path)
    if palindromes:
        return max(palindromes, key=len)
    return None

longest_palindrome_word = longest_palindrome('sowpods.txt')
print("Longest palindrome word:", longest_palindrome_word)

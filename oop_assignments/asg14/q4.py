def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
    palindromes = [word.strip() for word in words if is_palindrome(word.strip().lower())]
    return palindromes

palindromes = find_palindromes('sowpods.txt')
print("Palindrome words:", palindromes)

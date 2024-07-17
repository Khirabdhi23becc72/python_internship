def find_consonants(s):
    vowels = 'aeiou'
    consonants = [char for char in s if char.isalpha() and char.lower() not in vowels]
    return consonants

user_input = input("Enter a string: ")
consonants = find_consonants(user_input)
print("Consonants in the string:", consonants)

def count_letters_digits(s):
    letters = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    return letters, digits

user_input = input("Enter a sentence: ")

letters, digits = count_letters_digits(user_input)
print(f"LETTERS {letters} DIGITS {digits}")

def count_letters_digits_manual(s):
    letters = 0
    digits = 0
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            letters += 1
        elif '0' <= char <= '9':
            digits += 1
    return letters, digits

user_input = input("Enter a sentence: ")

letters, digits = count_letters_digits_manual(user_input)
print(f"LETTERS {letters} DIGITS {digits}")

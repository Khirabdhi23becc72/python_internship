def count_alphabets(s):
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count

user_input = input("Enter a string: ")

result = count_alphabets(user_input)
print("Number of alphabets:", result)

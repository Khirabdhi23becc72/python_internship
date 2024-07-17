def count_alphabets_manual(s):
    count = 0
    for char in s:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            count += 1
    return count

user_input = input("Enter a string: ")

result = count_alphabets_manual(user_input)
print("Number of alphabets:", result)

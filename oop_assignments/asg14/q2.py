import string

def find_non_consecutive_alphabets(file_path):
    all_alphabets = set(string.ascii_lowercase)
    consecutive_alphabets = set()
    with open(file_path, 'r') as file:
        words = file.readlines()
    for word in words:
        word = word.strip().lower()
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                consecutive_alphabets.add(word[i])
    non_consecutive_alphabets = all_alphabets - consecutive_alphabets
    return non_consecutive_alphabets

non_consecutive_alphabets = find_non_consecutive_alphabets('sowpods.txt')
print("Alphabets never appearing in sequence:", sorted(non_consecutive_alphabets))

def find_words_with_uu(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
    uu_words = [word.strip() for word in words if 'uu' in word]
    return uu_words

uu_words = find_words_with_uu('sowpods.txt')
print("Words containing 'uu':", uu_words)

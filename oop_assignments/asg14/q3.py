def words_with_all_vowels(file_path):
    vowels = set('aeiou')
    with open(file_path, 'r') as file:
        words = file.readlines()
    words_with_vowels = [word.strip() for word in words if vowels <= set(word.strip().lower())]
    return words_with_vowels

words_all_vowels = words_with_all_vowels('sowpods.txt')
print("Words containing all the vowels:", words_all_vowels)

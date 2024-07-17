def words_in_sonnet_not_in_sowpod(sonnet_file, sowpod_file):
    with open(sonnet_file, 'r') as sonnet:
        sonnet_words = set(word.strip().lower() for word in sonnet.readlines())
    with open(sowpod_file, 'r') as sowpod:
        sowpod_words = set(word.strip().lower() for word in sowpod.readlines())
    unique_sonnet_words = sonnet_words - sowpod_words
    return unique_sonnet_words

unique_sonnet_words = words_in_sonnet_not_in_sowpod('sonnet_words.txt', 'sowpods.txt')
print("Words in sonnet_words.txt but not in sowpods.txt:", unique_sonnet_words)

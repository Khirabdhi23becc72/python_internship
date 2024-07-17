def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Create an empty dictionary to store word frequencies
    words_freq = {}
    # Iterate through each word in the list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in words_freq:
            words_freq[word] += 1
        # If the word is not in the dictionary, add it with an initial count of 1
        else:
            words_freq[word] = 1
    # Print each word and its frequency
    print("Word frequencies:")
    for word, freq in words_freq.items():
        print(f"{word}: {freq}")

# Example sentence
sentence = "I like playing outside with my friends and playing games"

# Call the function to count word frequencies
count_words(sentence)

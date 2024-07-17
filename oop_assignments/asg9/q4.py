# define the function
def word_length_dict(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}

# get user input for sentence
sentence = input("Enter a sentence: ")

# use the word_length_dict function
word_lengths = word_length_dict(sentence)

# print the word lengths dictionary
print(word_lengths)

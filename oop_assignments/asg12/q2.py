import random
import string

# Function to generate a random alphabetical character
def random_alpha_char():
    return random.choice(string.ascii_letters)

# Function to generate a random alphabetical string of arbitrary length
def random_alpha_string(length=None):
    if length is None:
        length = random.randint(1, 100)  # Random length between 1 and 100 if not specified
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Function to generate a random alphabetical string of a fixed length
def random_fixed_length_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Example usage:
print("Random alphabetical character:", random_alpha_char())
print("Random alphabetical string of arbitrary length:", random_alpha_string())
print("Random alphabetical string of length 10:", random_alpha_string(10))
print("Random alphabetical string of fixed length 5:", random_fixed_length_string(5))

input_string = input("Enter a string: ")
index = int(input("Enter an index: "))

if 0 <= index < len(input_string):
    character = input_string[index]
    print("The character at index {index} is '{character}'")
else:
    print("Invalid index. Please enter a valid index within the range of the string.")
# define the function
def find_char(matrix, char):
    found = False
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    
    # handle the case in case of no inputs
    if num_rows == 0 or num_cols == 0:
        print("Not found")
        return

    # search the character
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if matrix[row_index][col_index] == char:
                print(f"Row: {row_index}, Column: {col_index}")
                found = True
                break
        if found:
            break

    # print not found if character is not found in the matrix
    if not found:
        print("Not found")

# get user input for matrix
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

# get user input for character
char = input("Enter the character to find: ")

# call the function
find_char(matrix, char)

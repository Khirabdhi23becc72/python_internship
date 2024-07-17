def matrix_multiplication(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if multiplication is possible
    if cols_matrix1 != rows_matrix2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

    # Initialize the result matrix with zeros
    result_matrix = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Perform the matrix multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Example usage
matrix1 = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]

result = matrix_multiplication(matrix1, matrix2)
print("Resultant Matrix:")
print_matrix(result)

def determinant_2x2(matrix):
    """
    Calculate the determinant of a 2x2 matrix.

    Parameters:
    matrix (list of list of int/float): A 2x2 matrix

    Returns:
    int/float: Determinant of the matrix
    """
    # Validate the input matrix
    if len(matrix) != 2:
        raise ValueError("Matrix must have 2 rows")
    if len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Matrix must have 2 columns in each row")
    
    # Extracting elements of the 2x2 matrix for clarity
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    # Debug statements to print the elements of the matrix
    print(f"Matrix elements: a={a}, b={b}, c={c}, d={d}")

    # Calculate the determinant using the formula: ad - bc
    determinant = a * d - b * c

    # Debug statement to print the calculated determinant
    print(f"Determinant: {determinant}")

    return determinant

# Example usage
matrix = [[1, 2], [3, 4]]
print("Input matrix:")
for row in matrix:
    print(row)

det = determinant_2x2(matrix)
print(f"Determinant of the matrix: {det}")

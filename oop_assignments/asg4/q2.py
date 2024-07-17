def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = add_matrices(matrix1, matrix2)
print("Resultant Matrix:")
for row in result:
    print(row)

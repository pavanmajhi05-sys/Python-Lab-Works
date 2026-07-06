def merge_matrices(matrix1, matrix2):
    merged_matrix = [[matrix1[i][j] + matrix2[i][j]
                       for j in range(len(matrix1[0]))]
                      for i in range(len(matrix1))]
    return merged_matrix

matrix1 = [[1,2],[3,4]]
matrix2 = [[5,6],[7,8]]
merged_matrix = merge_matrices(matrix1, matrix2)
print(merged_matrix)

with open('input.txt') as f:
    matrix = [list(map(int, row.split())) for row in f.readlines()]
matrix2 = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix2[j][i] = matrix[i][j]
with open('output.txt', 'w') as f:
  for row in matrix2:
    f.write(' '.join(map(str, row)) + '\n')
import copy

matrix = [[1, 1, 0, 1, 0],
          [0, 1, 1, 1, 0],
          [1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1]]

s = copy.deepcopy(matrix)
r, c = len(matrix), len(matrix[0])
m = 0

for i in range(1, r):
    for j in range(1, c):
        if matrix[i][j] == 1:
            s[i][j] = 1 + min(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1])
            m = max(m, s[i][j])

m
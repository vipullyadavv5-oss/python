matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
cols = len(matrix[0])

transpose = []

for j in xrange(cols):
    row = []
    for i in xrange(rows):
        row.append(matrix[i][j])
    transpose.append(row)

print(transpose)

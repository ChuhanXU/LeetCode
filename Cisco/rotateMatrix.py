def rotate(n):
    matrix = create(n)
    print(matrix)
    matrix.reverse()
    print(matrix)
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def create(n):
    matrix = [[0]*n for i in range(n)]
    m = 1
    for i in range(n):
        for j in range(n):
            matrix[i][j] = m
            m+=1
    return matrix
print(rotate(2))
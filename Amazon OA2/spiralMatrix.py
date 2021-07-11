# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
def generateMatrix(n):

    mat = [[None for _ in range(n)] for _ in range(n)]
    h1, h2 = 0, n-1
    v1, v2 = 0, n -1
    c = 1
    while h1 <= h2 and v1 <= v2:
        for i in range(v1, v2+1):
            mat[h1][i] = c
            c += 1
        h1 += 1
        for i in range(h1, h2+1):
            mat[i][v2] = c
            c += 1
        v2 -= 1
        for i in range(v2, v1 - 1, -1):
            mat[h2][i] = c
            c += 1
        h2 -= 1
        for i in range(h2, h1 - 1, -1):
            mat[i][v1] = c
            c += 1
        v1 += 1
    return mat
print(generateMatrix(3))
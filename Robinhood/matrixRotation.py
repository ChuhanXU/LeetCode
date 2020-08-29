
# 一个方矩阵， 一个int[] query,
# query[i] = 0则顺时针转90度，
# 1 则对角线翻转，
# 2 则逆对角线翻转，求最终矩阵输出
import numpy as np


def rotate(matrix,number):
    if number == 1:
        n,m = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(i,m,1):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    if number == 0:
        matrix = [[matrix[n-1-j][i] for j in range(n)]for i in range(m)]
    # rotated = np.rot90(matrix)
    if number == 2:
        for i in range(m-1,-1,-1):
            for j in range
    return matrix

matrix = [[2, 2, 3], [1, 1, 3], [2, 2, 4]]
print(rotate(matrix,1))

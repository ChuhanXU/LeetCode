
# 一个方矩阵， 一个int[] query,
# query[i] = 0则顺时针转90度，
# 1 则对角线翻转，
# 2 则逆对角线翻转，求最终矩阵输出
def rotate(matrix):
    n,m = len(matrix),len(matrix[0])


    rotated = [[matrix[n-1-j][i] for j in range(n)]for i in range(m)]
    return rotated

matrix = [[2, 2, 3], [1, 1, 3], [2, 2, 4],[1,2,5]]
print(rotate(matrix))

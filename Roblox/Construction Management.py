def mincost(matrix):
    n = len(matrix)
    if n==0:
        return 0
    for i in range(1,n,1):
        matrix[i][0] += min(matrix[i - 1][1], matrix[i - 1][2])
        matrix[i][1] += min(matrix[i - 1][0], matrix[i - 1][2])
        matrix[i][2] += min(matrix[i - 1][0], matrix[i - 1][1])
    return min(min(matrix[n-1][0],matrix[n-1][1]),matrix[n-1][2])

matrix=[[1,2,2],[2,2,1],[2,2,1]]

print(mincost(matrix))
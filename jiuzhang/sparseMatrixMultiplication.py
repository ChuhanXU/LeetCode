# 调整数据结构提高时间复杂度

# O(n^2)
def multiply(A,B):
    n = len(A)
    m = len(A[0])
    k = len(B[0])
        # [n*m]**[m*k]

        # row_vector 是一个有n个list的list，每一个list对应一个不为0的值，值的index和值的大小
 # O(mn)
    row_vector=[
        [
            (j,A[i][j]) for j in range(m) if A[i][j] != 0
        ]
        for i in range(n)
    ]
         # row_vector共有n个小list，每个小list遍历每一列
    # O(km)
    col_vector = [
        [(i,B[i][j]) for i in range(m) if B[i][j] != 0]
        for j in range(k)
    ]
         # col_vector共有k个小list，每个小list遍历每一行
        # 双指针 向量相乘
    # O(kn*1)
    C = [
        [
            multi(row,col) for col in col_vector
        ]
        for row in row_vector
    ]
    return C

# O(len(row)+len(col)) 假设非0元素是常数级
def multi(row, col):
    i = 0
    j = 0
    ans = 0
    while i<len(row) and j < len(col):
        index1,val1 = row[i]
        index2,val2 = col[j]
        # 通过if语句让A的每一行的第index个和B的每一列的第index相乘
        if index1 < index2:
            i+=1
        elif index1>index2:
            j+=1
        else:
            ans += val1 * val2
            i+=1
            j+=1
    return ans
A = [[1,0,0],[-1,0,3]]
B = [[7,0,0],[0,0,0],[0,0,1]]
print(multiply(A,B))






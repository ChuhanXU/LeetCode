class Matrix:
    def __init__(self):  # 零矩阵
        self.mat = [[0 for j in range(2)] for i in range(2)]

    def identityMatrix(self):  # 单位矩阵
        for i in range(2):
            for j in range(2):
                if i == j:
                    self.mat[i][j] = 1
                else:
                    self.mat[i][j] = 0

    def __mul__(self, m):  # 矩阵乘法的计算
        tmp = Matrix()
        for i in range(2):
            for k in range(2):
                if (self.mat[i][k] == 0):
                    continue
                for j in range(2):
                    tmp.mat[i][j] += self.mat[i][k] * m.mat[k][j]
                    tmp.mat[i][j] %= 10000;
        return tmp


class Solution:
    """
    @param n: an integer
    @return: return a string
    """

    def qpow(self, A, a):  # 矩阵快速幂
        B = Matrix()
        B.identityMatrix()
        while a > 0:
            if (a % 2 == 1):
                B = B * A
            A = A * A
            a //= 2
        return B

    def lastFourDigitsOfFn(self, n):
        if (n == 0):
            return 0
        A = Matrix()
        # 构造矩阵
        A.mat = [[1, 1], [1, 0]]
        m = self.qpow(A, n - 1)
        return m.mat[0][0]



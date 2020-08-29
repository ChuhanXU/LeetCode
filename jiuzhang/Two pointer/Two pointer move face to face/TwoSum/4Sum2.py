
# # O(n^2)来自四个不同的数组
# 因为只需要count所以可以减少复杂度
class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def fourSumCount(self, A, B, C, D):
        counter = {}
        for a in A:
            for b in B:
                counter[a + b] = counter.get(a + b, 0) + 1
        answer = 0
        for c in C:
            for d in D:
                answer += counter.get(-c - d, 0)
        return answer
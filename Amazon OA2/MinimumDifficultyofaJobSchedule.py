
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).
#
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.
#
# Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].
#
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
def minDifficulty(A, d):
    n = len(A)
    dp, dp2 = [float('inf')] * n, [0] * n
    if n < d: return -1
    for d in range(d):
        stack = []
        for i in range(d, n):
            dp2[i] = dp[i - 1] + A[i] if i else A[i]
            while stack and A[stack[-1]] <= A[i]:
                j = stack.pop()
                dp2[i] = min(dp2[i], dp2[j] - A[j] + A[i])
            if stack:
                dp2[i] = min(dp2[i], dp2[stack[-1]])
            stack.append(i)
        dp, dp2 = dp2, [0] * n
    return dp[-1]
# A=[6,5,4,3,2,1]
# d=2
A=[9,9,9]
d=4
print(minDifficulty(A,d))
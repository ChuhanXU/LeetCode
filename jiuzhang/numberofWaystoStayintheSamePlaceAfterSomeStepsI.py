#     #
#     # """
#     # @param steps: steps you can move
#     # @param arrLen: the length of the array
#     # @return: Number of Ways to Stay in the Same Place After Some Steps
#     # """
def dfs(now_pos, steps, arrLen):
    # new_pos 当前所在位置 ，steps：指针还需要移动的次数 arrLen 数组的长度
    # 在任意时候越界：该路径不是合法路径
    if  now_pos>=arrLen  or  now_pos< 0:
        return 0
    if steps == 0:
        if now_pos != 0:
            return 0
        return 1
    return (dfs(now_pos - 1, steps-1, arrLen) + dfs(now_pos +1, steps-1, arrLen) + dfs(now_pos, steps-1, arrLen));
def numWays(steps, arrLen):
        # write your code here
        return dfs(0,steps, arrLen)



print(numWays(3,2))

# # 动态规划的方法
# def numWays(steps, arrLen):
#     MOD = 1000000007
#         # 最远能走到的位置
#     furthestPos = int(min(steps / 2, arrLen - 1))
#     # (furthestPos + 1) 代表位置的数量 [0]代表初始值都为0
#     dp = [[0] * (furthestPos + 1) for _ in range(steps + 1)]
#     # 将 dp(0, 0) 初始化为 1，代表走 0 步在 0 位置的方案数是 1
#     dp[0][0] = 1
#
#     for i in range(1, steps + 1):
#         for j in range(furthestPos + 1):
#             # 加上从第 i - 1 步向右走到 j 的方案数
#             # 当j<=0的时候不能向左走
#             if j > 0:
#                 dp[i][j] += dp[i - 1][j - 1]
#                 dp[i][j] = dp[i][j] % MOD
#
#             # 加上从第 i - 1 步向左走到 j 的方案数
#             # 当 j >= furthestPos 的时候不能继续向右走
#             if j < furthestPos:
#                 dp[i][j] += dp[i - 1][j + 1]
#                 dp[i][j] = dp[i][j] % MOD
#
#             # 加上站在原地的方案数
#             dp[i][j] += dp[i - 1][j]
#             dp[i][j] = dp[i][j] % MOD
#
#     return dp[steps][0]

# # dp = [[0] * (2) for _ in range(3)]
# #
# # print(5/2)
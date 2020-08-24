
# 有点像houserubber
def njar(nums):
    n= len(nums)
    if(n==0):
        return 0
    dp = [[0]*2 for i in range(n)]
    dp[0][0]=0
    dp[0][1]=nums[0]


    for i in range(1,len(nums)):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1])
        dp[i][1]=nums[i]+dp[i-1][0]
        result = max(dp[n-1][0],dp[n-1][1])
    return result
nums=[5,30,99,60,5,10]
print(njar(nums))
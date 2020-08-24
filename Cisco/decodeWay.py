
# Given a string of digits as input, print out the number of valid interpretations of letters
# write a function to calculate the number of valid interpretation of the letters formed by the
# given input

# input 100200300
# starting from 0 to 25
# output 4
# ("1","0","0","2","0","0","3","0","0")
# ("10","0","2","0","0","3","0","0")
# ("1","0","0","20","0","3","0","0")
# ("10","0","20","0","3","0","0")
# 划分型动态规划问题
s=input()

def decodeWay(s):
    if s == '':
        return 0
    dp = [1,1]
    for i in range(2,len(s)+1):
        dp.append(0)

        if 10 <= int(s[i-2:i]) <= 26:
            dp[i]+=dp[i-2]

        if 0 <= int(s[i-1:i]) <= 9:
            dp[i] += dp[i-1]
    return dp[-1]
print(decodeWay(s))
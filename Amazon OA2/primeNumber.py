
# input string 11373
# output 6
# [11,3,7,3][113,7,3][11,37,3][113,73][11,373]
# dynamic algorithm
import math
from math import ceil
memo = {}
dp = {0: False, 1: False, 2:True, 3: True}
def isPrime(n):
    if n in dp:
        return dp[n]
    v = int(ceil(math.sqrt(n)))
    for i in range(2, v+1):
        if n % i == 0:
            dp[n] = False
            return False
    dp[n] = True
    return True

def bt(s):
    if not s:
        return 1
    if s in memo:
        return memo[s]
    val = ''
    total = 0
    for i in range(len(s)):
        val += s[i]
        if isPrime(int(val)):
            total += bt(s[i+1:])

    memo[s] = total
    return memo[s]



s = '5211'

print(bt(s))

# 5 211
# 5 2 11
print(isPrime(211))

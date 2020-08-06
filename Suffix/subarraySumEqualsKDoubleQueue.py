import collections

# 一个双端队列d，变量i从0开始到n（包含）遍历，队列中存放的是0,i之间可能的开始位置，i为结束位置。
# 如果d0满足条件（就是d0开始，i结束的字数组和至少为K），就删除它，然后再循环判断，直到d0不满足条件。
# d中位置对应的值是从小到大的，0不满足，后面更不可能满足，所以不用再判断。 如果i比队尾元素小或相等，就删除队尾，循环判断，直到i比队尾元素大。
def shortestSubarray(A, K):
    # Write your code here.
    N = len(A)
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    d = collections.deque()
    res = N + 1
    for i in range(N + 1):
        while d and B[i] - B[d[0]] >= K:
            res = min(res, i - d.popleft())
        while d and B[i] <= B[d[-1]]:
            d.pop()
        d.append(i)
    return res if res <= N else -1
print(shortestSubarray([2,1,-1,4,2,-3],3))
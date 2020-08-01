
# Given an array of integers and an integer k, you need to find the minimum size of continuous subarrays whose sum equals to k, and return its length
# 这个题不能用双指针，因为可能会有负数，使用双指针的条件是通过移动指针可以保持变化一致，比如如果有负数的话，向右移动会导致区间和变小，而不是一直增大
# 时间复杂度O(n^2) 如何优化？ 想想哪些地方是多做的？
# 假设终点已经被确定了，我们只需要找到前缀和值为(pre_sum[j]-target)的前缀和值的位置就可以了
# 因为需要让区间长度最小，因此只要快速找到最近就可以了
# 前缀和通常会和哈希表(map或dic)合用
# 用一个哈希表来记录前j个元素里面前缀和是多少的index是多少
import sys
def subarraySumEqualsK(nums,k):
    n = len(nums)
    if n == 0:
        return -1
    prefix_sum = 0
    hashmap = {0:-1} # prefix_sum_value -> index
    # 加入前缀和数组是prefix = [1,3,1,7,5]
    # hashmap = {1:2,3:1,7:3,5:4} 会不断被更新,
    # 一个需要注意的地方：
    # 当输入为[1,2]时 k=3 找不到
    # {1:0,3:1}
    # need = 3 - 3 = 0,但是hashmap里找不到一个为0的前缀和，但其实是存在的，所以我们要加一个{0:-1}
    # 为什么是-1呢？
    # prefix_sum = 3的时候 i=1 i-?=2 ? = -1 need =0 所以hashmap[0]=-1
    ans = sys.maxsize
    for i in range(n):
        prefix_sum += nums[i]
        need = prefix_sum - k
        if need in hashmap:
            ans = min(ans,i - hashmap[need])
        hashmap[prefix_sum]=i

    # prefix = [0] *n
    # for i in range(n):
    #     if i == 0:
    #         prefix[i]=nums[i]
    #         continue
    #     prefix[i] = prefix[i-1]+nums[i]
    #     # 枚举每个区间
    # #     最小的子数组长度
    # ans = sys.maxsize
    # for i in range(n):
    #     for j in range(i,n):
    #         if i == 0:
    #             if prefix[j] == k:
    #                 # prefix[5]是前六个数的和，包括0和5
    #                 ans = min (j+1,ans)
    #             continue
    #         if prefix[j]-prefix[i] == k:
    #             ans = min(ans,j-i)
    if ans == sys.maxsize:
        return -1
    return ans
print(subarraySumEqualsK([2,1,-1,4,2,-3],3))

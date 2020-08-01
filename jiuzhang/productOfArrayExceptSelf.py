# 求出除了这个数，数组中其它数的乘积
# [1,2,3,4] [24,12,8,6]
# 使用前缀积的思想，先分别算出前缀积和后缀积
# 注意后缀积  for i in range (n-1,-1,-1):
# 最后合并的时候要注意数组越界问题
# 前缀和唯一可以优化的地方是空间，不开前缀和的数组
# 如何将前缀和后缀积数组都去掉？
# 遍历两边output，第一边将前缀放进去，第二遍将后缀放进去
def productExceptSelf(nums):
    n = len(nums)
    now_multi = 1
    if n == 0:
        return []
    # # 计算前缀和
    # prefix = [1] * n
    # for i in range(n):
    #     if i == 0:
    #         prefix[i]=nums[i]
    #     else:
    #         prefix[i]=prefix[i-1]*nums[i]
    # 计算后缀和
    suffix = [1] * n
    for i in range (n-1,-1,-1):
        if i == n-1:
            suffix[i] = nums[i]
        else:
            suffix[i] = suffix[i+1]*nums[i]
    output = [1]*n
    # 可以不用前缀数组，加一个now_multi

    for i in range(n):

        if i == 0:
            output[i]=suffix[i+1]
            continue
        if i == n-1:
            output[i]=now_multi

            # output[i]=prefix[i-1]
            continue
        output[i] = now_multi * suffix[i + 1]
        # output[i] = prefix[i-1]*suffix[i+1]
        now_multi *= nums[i]
    return output

print(productExceptSelf([1,2,3,4]))

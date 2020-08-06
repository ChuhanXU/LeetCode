# 遍历两边output，第一边将前缀放进去，第二遍将后缀放进去,优化时间复杂度
# 多次更新答案 来优化空间
def productExceptSelf(nums):
    n = len(nums)
    if n == 0:
        return[]
    output = [1]*n
    now_multi = 1
    # 前i-1个元素之积
    for i in range(n):
        output[i] *= now_multi
        now_multi *= nums[i]
    now_multi = 1
    # 后i+1个元素之积
    for i in range(n-1,-1,-1):
        output[i]*=now_multi
        now_multi*=nums[i]
    return output
print(productExceptSelf([1,2,3,4]))
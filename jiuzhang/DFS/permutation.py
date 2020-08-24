def permute(nums):
    results = []

    # 如果数组为空直接返回空
    if nums is None:
        return []

    # dfs
    used = [0] * len(nums)
    dfs(nums, used, [], results)
    return results


def dfs(nums, used, current, results):
    # 找到一组排列，已到达边界条件
    if len(nums) == len(current):
        # 因为地址传递，在最终回溯后current为空导致results中均为空列表
        # 所以不能写成results.append(current)
        results.append(current[:])
        return

    for i in range(len(nums)):
        # i位置这个元素已经被用过
        if used[i]:
            continue

        # 继续递归
        current.append(nums[i])
        used[i] = 1
        dfs(nums, used, current, results)
        # 回溯
        used[i] = 0
        current.pop()
nums = [1,2,3]
print(permute(nums))
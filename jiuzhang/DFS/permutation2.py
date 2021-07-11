# 相比不重复的元素，一定要排序
def permuteUnique(nums):
    if not nums:
        return [[]]
    visited = [False]*len(nums)
    results = []
    nums = sorted(nums)
    dfs(nums, visited, [], results)
    return results


def dfs(nums, visited, current, results):
    if len(nums) == len(current):
        results.append(current[:])
        return
    for i in range(len(nums)):
        if (i > 0 and nums[i] == nums[i - 1] and visited[i - 1]==False) or visited[i] == True:
            continue
        current.append(nums[i])
        visited[i]=True
        dfs(nums, visited, current, results)
        current.pop()
        visited[i]=False
nums=[2,2,1,1]
print(permuteUnique(nums))
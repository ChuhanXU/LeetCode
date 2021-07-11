# 输入：[1,2,3]
# 输出：
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

def subsets(nums):
    nums = sorted(nums)
    results = []
    dfs(nums, 0, [], results)
    return results


def dfs(nums, index, current, results):
    results.append(current[:])

    for i in range(index, len(nums)):
        # 避免重复的subset，当我选了第二个2却没选第一个2的时候需要continue index=1，i=2 i>index
        if i!=0 and nums[i]==nums[i-1] and i!=index:
            continue
        current.append(nums[i])
        dfs(nums, i + 1, current, results)
        current.pop()
nums=[1,2,2,3]
print(subsets(nums))



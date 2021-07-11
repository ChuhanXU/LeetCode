# 保证没有重复，如果要用visited.add的话，不然要用used数组通过位置来区分两个相同的数
def permute(nums):
    if not nums:
        return [[]]
    results=[]
    dfs(nums, set(), [], results)
    return results

def dfs(nums, visited, current, results):
    # 找到一组排列，已到达边界条件
    if len(nums) == len(current):
        # 因为地址传递，在最终回溯后current为空导致results中均为空列表
        # 所以不能写成results.append(current)
        results.append(current[:])
        return

    for num in nums:
        if num in visited:
            continue

        # 继续递归
        current.append(num)
        visited.add(num)
        dfs(nums, visited, current, results)
        # 回溯
        visited.remove(num)
        current.remove(num)
nums = [1,2,3]
print(permute(nums))
s="ab"
print(list(s))

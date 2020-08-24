# input = (3,2)
# [1,2,3] 中 2个数的 组合
# output = [1,2] [1,3] [2,3]
def combination(n,k):
    if n == 0 or k == 0:
        return []
    nums = []
    for i in range (1,n+1):
        nums.append(i)

    result = []
    dfs(nums,[],k,result,0)
    return result

def dfs(nums,current,k,result,index):
    if k==0:
        result.append(current[:])
        return

    for i in range(index,len(nums)):
        current.append(nums[i])


        dfs(nums,current,k-1,result,i+1)
        # dfs(nums, current, k - 1, result, index + 1)

        current.pop()
print(combination(3,2))
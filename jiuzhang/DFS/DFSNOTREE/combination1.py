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
    dfs(nums,0,[],result,k)
    return result

def dfs(nums,index,current,result,k):
    if k==0:
        result.append(current[:])
        return

    for i in range(index,len(nums)):
        current.append(nums[i])
        dfs(nums,i+1,current,result,k-1)
        current.pop()
print(combination(5,2))
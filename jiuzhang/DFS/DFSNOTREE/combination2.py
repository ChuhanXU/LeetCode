
# you are given a set of candidates and a target, you need to find all combination
# that satisfy the sum of candidate equal to target

# input candidates = [2,3,6,7],target = 7
# output [[7],[2,2,3]]
# possible questions:
# 1.what is your given?
# 2.what should I return as result if the n or m == 0?
# 3.do we have duplications in our candidate set?
# 4.do we need to care about the order of element in the combination or the combinations in the result list
# is it Okay if the time complexity is n to the m power which n is the number of elements in candidates and
# target equal the number of combinations in out put , the max number will be target/min

# for this kind of problem which we need to search all of the results that satisfy our conditions.
# we uauslly use dfs to solve it in case of leakage solutions
# since numbers in combination must be in non-descending order we first need to make our candidate in ascending order

# 组合问题的dfs模板
# def combinationSum(nums,限制条件):
#     if len(nums)==0:
#         return
#     result=[]
#     # dfs(nums,index,current,result,一个限制条件比如要求每个组合包含k个元素，或者组合的和为某个数)
#     dfs(nums,0,[],result,限制条件)
#     return result
# def dfs(nums,index,current,result,限制条件):
#     出口：当满足限制条件时,result.append()
#     if remainTarget==0 或者 k==0(k是指如果要求集合元素数量的情况)
#       result.append(current[:])
#       return
#     拆解：用for循环进行拆解，依次往后推一个元素，重复一样的操作
#     for i in range(index,len(nums)):
#     这里可能会有限制条件，比如求和问题  if nums[i]>remainTarget: return
#
#       current.append(nums[i])
#     i+1 是因为要求每一个元素不能使用两次，如果为i则说明可以重复使用
#     限制条件要根据题意推断，如果是控制数量 k-1，如果是和 remainTarget-nums[i]
#       dfs(nums,i+1,current,result,限制条件的变化)
#      最后一定要记得回溯
#      current.pop()

def combinationSum(candidates,target):
    if len(candidates) == 0:
        return []
    nums = sorted(candidates)
    result = []
    dfs(nums,[],result,target,0)
    return result
def dfs(nums,current,result,remainTarget,index):
    if remainTarget == 0:
        # we need to do a deep copy here in case of the final result will be changed
        result.append(current[:])
        return
    for i in range(index,len(nums)):
# we need to determin if we can put the nums[i] in current, what is the judge condition
        if nums[i]>remainTarget:
            return
        current.append(nums[i])
        # we need to pass i as our next index not i+1,because we can use elements in candidate set many times
        dfs(nums,current,result,remainTarget-nums[i],i)
        current.pop()
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))

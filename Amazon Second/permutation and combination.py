# O(n!)
def permutation(nums):
    if len(nums)==0:
        return []
    result = []
    visited=set()
    current=[]
    dfs(nums,visited,current,result)
    return result
def dfs(nums,visited,current,result):
    if len(nums)==len(current):
        result.append(current[:])
        return
    for num in nums:
        if num in visited:
            continue
        current.append(num)
        visited.add(num)
        dfs (nums,visited,current,result)
        current.pop()
        visited.remove(num)
nums=[1,2,3]
print(permutation(nums))

# def combination(nums, k):
#     if len(nums) == 0:
#         return []
#     result = []
#
#     current = []
#     dfs(nums, 0, current, result, k)
#     return result
#
#
# def dfs(nums, index, current, result, k):
#     if k == 0:
#         result.append(current[:])
#         # return
#     for i in range(index, len(nums)):
#         current.append(nums[i])
#         dfs(nums, i + 1, current, result, k - 1)
#         current.pop()


nums = [1, 2, 3]
# print(combination(nums, 2))
# print(permutation(nums))
# k current[]
# exit if len(current)==k append the current to the result and return
# [1,2,3]
# index =0
# [1,]
# index=1
# [1,2]

#   O(2^n)
class Solution:
    def combination(self,nums,target):
        if len(nums)==0:
            return []
        index=0
        current=[]
        result=[]

        self.dfs(nums,index,current,result,target)
        return result
    def dfs(self,nums,index,current,result,target):
        if target==0:
            if current not in result:
                result.append(current[:])
                return
        for i in range(index,len(nums)):
            current.append(nums[i])
            self.dfs(nums,i+1,current,result,target-nums[i])
            current.pop()
nums = [1, 2, 3]
solution = Solution()
print(solution.combination(nums, 4))

# [1,2,3] 2
# 0 1 2
# cur [1]

# index = 1 k=1
# 1 2
# cur [1,2]      cur[1,3]
#                result [[1,2],[1,3]]
#                cur[1]

# index=2 k=0
# return
# result:[[1,2],]
# cur [1]

# [1] 1 2
# [1,2]  2 return




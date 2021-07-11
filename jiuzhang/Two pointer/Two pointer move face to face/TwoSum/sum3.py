# # https://www.jiuzhang.com/problem/3sum/#tag-lang-python
# # a+b+c=0
# class Solution:
#     """
#     @param numbers: Give an array numbers of n integer
#     @return: Find all unique triplets in the array which gives the sum of zero.
#     """
#
#     def threeSum(self, nums):
#         nums = sorted(nums)
#
#         results = []
#         for i in range(len(nums)):
#             # 跳过重复的数
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             # 将第i数设置为负，然后在[i+1,len(nums)-1]中找和为-nums[i]的数
#             self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], results)
#
#         return results
#
#     def find_two_sum(self, nums, left, right, target, results):
#         # 记录结果，防止重复
#         last_pair = None
#         while left < right:
#             if nums[left] + nums[right] == target:
#                 if (nums[left], nums[right]) != last_pair:
#                     results.append([-target, nums[left], nums[right]])
#                 last_pair = (nums[left], nums[right])
#                 right -= 1
#                 left += 1
#             elif nums[left] + nums[right] > target:
#                 right -= 1
#             else:
#                 left += 1
# solution = Solution()
# nums = [-1,-1,2,0,1,-2,2]
# print(solution.threeSum(nums))
def sum(array,target):
    if not array:
        return -1
    array=sorted(array)
    result = []
    for i in range(len(array)):
        # if i>0 and array[i-1]==array[i]:
        #     continue
        helper(array,i+1,len(array)-1,target-array[i],result,target)
    return result
def helper(array,left,right,a,result,target):
    while left<right:
        if array[left]+array[right]==a:
            if (target-a,array[left],array[right]) not in result:
                result.append((target-a,array[left],array[right]))
            left+=1
            right-=1
        elif array[left]+array[right]>a:
            right -= 1
        else:
            left+=1
nums = [-1,-1,2,0,1,-2,2]
print(sum(nums,-2))

# [2,3,4,6,12] 9
#if it is none
# two pointer
# mindiff
# result
import sys


def twoCloseTarget(nums,target):
    if len(nums)==0:
        return[]
    nums = sorted(nums)
    left = 0
    right = len(nums)-1
    mindiff = sys.maxsize


    while left<right:
        if nums[left]+nums[right]>target:
            diff = (nums[left]+nums[right])-target
            if diff < mindiff:
                mindiff = diff
                ans=[nums[left],nums[right]]
            right-=1
        elif nums[left]+nums[right]<target:
            diff = target-(nums[left]+nums[right])
            if diff < mindiff:
                mindiff = diff
                ans=[nums[left],nums[right]]
            left-=1
        else:

            return[nums[left],nums[right]]
    return ans
nums=[2,3,4,6,12]
print(twoCloseTarget(nums,9))

# class Solution:
#     # @param {int[]} nums an integer array
#     # @param {int} target an integer
#     # @return {int} the difference between the sum and the target
#     def twoSumClosest(self, nums, target):
#         # Write your code here
#         nums.sort()
#         i, j = 0, len(nums)  - 1
#
#         diff = 0x7fffffff
#         while i < j:
#             if nums[i] + nums[j] < target:
#                 diff = min(diff, target - nums[i] - nums[j])
#                 i += 1
#             else:
#                 diff = min(diff, nums[i] + nums[j] - target)
#                 j -= 1
#
#         return diff

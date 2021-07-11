# O(n)
class Solution(object):
    def rob(self, nums):
        prev = curr = 0
        for num in nums:
            temp = prev # This represents the nums[i-2]th value
            prev = curr # This represents the nums[i-1]th value
            curr = max(num + temp, prev) # Here we just plug into the formula
        return curr
#        tem pre
nums = [2, 7, 9, 3, 1]
# temp=prev
# prev=curr
# cur=max(pre,num+tem)
# return cur
solution = Solution()
print(solution.rob(nums))
class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if len(nums) == 0:
    #         return 0
    #     nums = sorted(nums)
    #
    #     length = 1
    #     for i in range(1, len(nums)):
    #         if nums[i] == nums[i - 1]:
    #             continue
    #
    #         length += 1
    #     return length
    def removeDuplicates(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        length = 0
        visited=[]
        for num in nums:
            if num in visited:
                continue
            visited.append(num)
            length+=1
        return length
nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
print(solution.removeDuplicates(nums))

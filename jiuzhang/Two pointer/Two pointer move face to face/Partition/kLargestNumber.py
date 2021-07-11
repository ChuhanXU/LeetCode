# quicksort 平均时间复杂度为O(n),在第一次快排以后，选取左边或右边在进行while，不用对两边同时进行
# O(N)+O(N/2)+O(N/4)+O(N/8)
# 做颜色分类和median
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, k, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        result = self.quickSort(nums, k, 0, len(nums) - 1)
        return result

    def quickSort(self, nums, k, start, end):
        # 当区间只剩下一个的时候，就找到了
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if  k < right:
            return self.quickSort(nums, k, start, right)
        if k > left:
            return self.quickSort(nums, k ,left, end)

        else:
            return nums[k-1]
nums = [1,5,8,-1]
soultion = Solution()
print(soultion.kthLargestElement(2,nums))

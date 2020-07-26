# 有序数组旋转求最小值是变相的二分法查找
class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        if not nums:
            return -1


        start, end = 0, len(nums) - 1
        # 如果第一个数小于第二个数，说明数组是有序的
        if nums[start]<nums[end]:
            return nums[start]
        # 如果nums[left] > nums[mid]，可以证明此时数组右半边是升序的，那我们就不用考虑右半边了。最小值一定在[left, mid]
        # 间，令right = mid。
        # 如果nums[left] <= nums[mid]，可以证明此时数组左半边是升序的，于是我们不需要考虑左半边。最小值一定在(mid, right]间，令left = mid + 1。
        # 直到left == right时，此时指向的就是最小值，return nums[left]。
        while start + 1 < end:  # 用来控制区间大小
            mid = (start + end) // 2
            if nums[start] >= nums[mid] :  # 如果mid位置上的数字小于等于最右端的数字时，区间向左移动
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])

    print (findMin(object,[4, 5, 6, 7, 0, 1, 2]))
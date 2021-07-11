
# quickSelect 相当于 有条件的quickSort 因为quickSort在完成一遍数组遍历的时候，还要再数组的两边分别进行同样的操作，但是quickSelect可以有选择的进行左边或者右边
# quickSort O(nlogn) quickSelectO(n)
# 就是quickSelect算法，适用于快速找到第K大元素或中位数
def selectMedian (nums):
    n = len(nums)
    if n == 0:
        return -1
    if n%2 == 0:
        return float((helper(nums, 0, n - 1, n//2)+helper(nums, 0, n - 1, n//2+1))/2)
    if n%2 == 1:
        return helper(nums, 0, n - 1, n//2+1)

def helper(nums,start,end,k):
    # 出口
    if start == end:
        return nums[start]

    left, right = start, end
    pivot = nums[left + (right - left) // 2]

    while left <= right:
        while left <= right and nums[left] < pivot:
            left+=1
        while left <= right and nums[right]> pivot:
            right-= 1
        if left <= right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right -= 1
#     left 和 right 已经交错，有三种区间的可能性
#     为什么+1，因为当k=1的时候实际找的是的第0个数
    if start + k -1 <= right:
        return helper(nums,start,right,k)
    # k-(left-start)是因为如果k在右半边的话，现在left的位置是第一个，要去掉前面的数
    if start + k-1 >= left:
        return helper(nums,left,end,k-(left-start))
    else:
        return nums[right+1]
nums = [-1,7,2,5,6,7]
print(selectMedian(nums))



# quickSelect 相当于 有条件的quickSort 因为quickSort在完成一遍数组遍历的时候，还要再数组的两边分别进行同样的操作，但是quickSelect可以有选择的进行左边或者右边
# quickSort O(nlogn) quickSelectO(n)
# 就是quickSelect算法，快速找到第K大元素
def selectMedian (nums):
    n = len(nums)
    if n == 0:
        return -1
    if n%2 == 0:
        return float((helper(nums, 0, n - 1, n//2)+helper(nums, 0, n - 1, n//2+1))/2)
    if n%2 == 1:
        return helper(nums, 0, n - 1, n//2+1)




def helper(nums,start,end,k):
    if start == end:
        return nums[start]
    left, right = start, end
    while left <= right:
        mid = left+(right-left)//2
        pivot = nums[mid]
        while left <= right and nums[left]>pivot:
            left+=1
        while left <= right and nums[right]< pivot:
            right-= 1
        if left <= right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right -= 1
#     left 和 right 已经交错，有三种区间的可能性
    if start + k -1 <= right:
        return helper(nums,start,right,k)
    if start +k-1 >= left:
        return helper(nums,left,end,k-(left-start))
    else:
        return nums[right+1]
nums = [1,2,3,4,5,6]
print(selectMedian(nums))


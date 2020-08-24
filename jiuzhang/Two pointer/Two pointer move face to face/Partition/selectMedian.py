
# 基本思想
# 先整体有序然后局部有序的思想
# 宏观上有序后再递归的调用分别针对左半部分和右半部分
# <=p的在左边 >=p的在右边,避免一种极端情况,就是数组中存在大量的相同数字,会出现不均匀的情况
# 最好是两端可以均分,避免时间复杂度退化的O(n^2)
# quicksort 不稳定
# O(nlog(n))  O(1)
def quickSort(nums):
    if len(nums)==0:
        return
    nums = helper(nums,0,len(nums)-1)
    return nums

def helper(nums,start,end):
    if start > end:
        return
    left,right = start,end
    # 这应该是一个随机数,最好能保证将数组均分
    # get value not index
    pivot = nums[(start+end)//2]
    # 20-27 partition的用法
    # left <= right 不是 left < right 会出现stack overflow的问题
    # 3 2 1 4 5 left = 3 right = 5 pivot = 1
    # 加上等号,可以使两个指针错开,不能存在交集
    # 不能是 nums[left] <= pivot ,想象全部都是1 左指针会一直走到最右边,造成分布不均匀
    # 应该停下来进行交换,虽然是无用功,但可以保证两个1 一边一个
    while left<=right and nums[left] < pivot:
        left += 1
    while left <= right and nums[right] > pivot:
        right -= 1
    if left <= right:
        nums[left],nums[right]=nums[right],nums[left]
        left  += 1
        right -= 1
#     完成这一步后 right,left 已经交错了,继续往两边递归
    helper(nums,start,right)
    helper(nums,left,end)
    return nums
nums=[3,5,3,1,5,6,0]
print(quickSort(nums))




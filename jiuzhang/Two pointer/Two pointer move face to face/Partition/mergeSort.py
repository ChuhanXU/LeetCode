
# 先局部排序再整体排序
# 分治思想,先无脑的中间切一刀,然后合并
# 需要花费额外的空间,因为有一个合并的过程
# O(nlog(n)) O(n)
# the main idea of merge sort is how to merge to sorted array, in merge sort the shortest sorted array
#  may be a single number
# 1 2 5 3 2 ->start=1, end=2
# 左半部分mergeSort(nums,start,(start+end)//2,temp)->(nums,0,2,temp)->(nums,0,1,temp)->(nums,0,0,temp)-> return得到了1
# 右半部分mergeSort(nums,(start+end)//2+1,end)->(nums,1,1)
# 稳定性
def mergesort(seq):
    if len(seq) <= 1:
        return seq

    mid = len(seq) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)
def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
seq = [1,2,5,3,2]
print(mergesort((seq)))


# def mergeSort(nums):
#     if len(nums)==0:
#         return
#     temp = [0]*len(nums)
#     result = helper(nums,0,len(nums)-1,temp)
#     return result
#
#
# def helper(nums,start,end,temp):
#     # 等于的情况下也不能拆解了
#     if(start >= end):
#         return
#     helper(nums,start,(start+end)//2,temp)
#     helper(nums, (start+end)//2+1, end, temp)
#     merge(nums,start,end,temp)
#
#
#
# def merge(nums,start,end,temp):
#     middle = (start+end)//2
#     leftStart = start
#     rightStart = middle+1
#
#     while leftStart <= middle and rightStart <= end:
#         if nums[leftStart]<nums[rightStart]:
#             temp[leftStart]=nums[leftStart]
#             leftStart+=1
#         else:
#             temp[rightStart]=nums[rightStart]
#             rightStart+=1
#     while leftStart <= middle:
#         temp[leftStart]=nums[leftStart]
#         leftStart += 1
#     while rightStart <= end:
#         temp[rightStart]=nums[rightStart]
#         rightStart += 1
#     return temp
# nums=[1,2,5,3,2]
# print(mergeSort(nums))





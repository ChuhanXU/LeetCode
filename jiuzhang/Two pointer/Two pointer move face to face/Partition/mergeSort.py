
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
    print(left)
    print(right)
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
        if left[i] <right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 很重要！若两个数组长度不一致，则会剩下一些剩余数字，将这些剩余数字加入数组
    result += left[i:]
    result += right[j:]
    print(result)
    return result
seq = [1,2,5,3,2,6,7,8,6]
print(mergesort((seq)))











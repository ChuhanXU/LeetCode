
# 先用partition将正负数分开，负数多的话就负数在前，否则正数在前，可以用一个flag判断谁在前
# 最后interleave即可
# AAAABBB   ABABABA 不相等的话就是第2个元素和最后一个元素换，第四个元素和倒数第三个换，每次两个
# AAABBB    ABABAB 相等的话就是第和倒数第二，第四和倒数第四
# input[-1,-2,-3,4,5,6]
# output[-1,5,-2,4,-3,6]
# 如果不用额外的空间就只能用比较的方法

def rerange(A):
    pos = len([a for a in A if a >0])
    neg = len(A) - pos

def partition(A,start_position):
    flag = 1 if start_position else -1
    left,right = 0,len(A)-1
    while left <= right:
        while left <= right and A[left]*flag >0:
            left += 1
        while left<= right and A[right]*flag <0:
            right -= 1
        if left <= right:
            A[left],A[right]=A[right],A[left]
            left+=1
            right-=1

def interval(A,has_same_length):
    left,right = 1,len(A)-1
    if has_same_length:
        right = len(A)-2
    while left <right:
        A[left], A[right] = A[right], A[left]
        left,right = left+2,right -2




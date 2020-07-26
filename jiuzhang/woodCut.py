# 什么时候用二分法？
# 当题目中要求出现求最大最小值的时候要想到二分法
def woodCut(L, k):
    # 如果数组为空
    if not L:
        return 0
    # 每段木头的最小值为1，因此每段木头的长度之和sum(L)一定要大于要求分的段数k
    if sum(L)<k:
        return 0

    start, end = 1, max(L)
    while start + 1 < end:
        mid = (start + end) // 2
        # 当分得的木头段数 >k 时，说明每一段分小了，因此要取后半部分，向右移动左指针
        # mid这里是打算分的长度
        if get_pieces(L, mid) >= k:
            start = mid
        # 当分得的木头段数 <k 时，说明每一段分小了，因此要取前半部分，向左移动右指针
        else:
            end = mid
    # 当分到只剩下114和115的时候, 判断两个长度哪个满足条件
    if get_pieces(L, end) >= k:
        return end
    if get_pieces(L, start) >= k:
        return start

    return 0


def get_pieces(L, length):
    pieces = 0
    for l in L:
        pieces += l // length
    return pieces

print(woodCut([232,124,456],7))
# print(sum([232,124,456]))
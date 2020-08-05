# 双指针模板
# i是左指针，j是右指针
# j = 0
# for i in range(n):
#     while j < n and i,j的搭配不满足条件
#         j+=1
#     处理 i，j这次搭配

class DataType:
    BAD = 1
    GOOD = 0
def maxSatisfied(customers, grumpy, X):
    n = len(customers)
    if n == 0:
        return 0

    left = 0
    right = X-1
    # 计算出前三天坏脾气的人数
    now_sum = 0
    for i in range (X):
        if grumpy[i] == DataType.BAD:
            now_sum += customers[i]
    # 所有区间内的最大差评人数
    # maximum_bad_number = now_sum 不能等于 0，因为如果grumpy是[1,1,1]刚好为三天会进入不了while循环，因此要把初始
    # 值设为3以满足这种情况
    maximum_bad_number = now_sum
#     双指针
#     这样写是为了防止out of boundary of array, 因为如果是while right < n,当right指向数组最后一个时
#     right = n+1 会越界，所以右指针的最大位置是数组倒数第二个
    #   while right < n
    while right  < n -1:
        right += 1
        if grumpy[right]==DataType.BAD:
            now_sum += customers[right]
        if grumpy[left] == DataType.BAD:
            now_sum -= customers[left]
        left += 1

        maximum_bad_number = max(maximum_bad_number,now_sum)

#    算出最终结果，原本好评的客人加上最大转变想法的客人
    satisfied_number = 0
    for i in range(n):
        if grumpy[i] == DataType.GOOD:
            satisfied_number += customers[i]
    return satisfied_number + maximum_bad_number

print(maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
# 第一种双指针写法[left,right] = 表示目标区间
# 第一种双指针写法[left,right) = 表示目标区间
# 第三种实现双指针的写法，while嵌套，这是一个常规写法

# 1.普通的sliding window,需要定义才开始的区间初始值，因为left right不是从0开始
# 2. 另一种定义区间的方法(一开一闭)，推荐使用两闭
# 3. 用通向双指针模板

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
    right = 0

    now_sum = 0
    maximum_bad_number = now_sum



    for left in range(n):
        while right < n and right-left < X:
        # 右指针移动
            if grumpy[right]==DataType.BAD:
                now_sum += customers[right]
            right += 1
        #     处理这次搭配
        maximum_bad_number = max(maximum_bad_number, now_sum)
        if grumpy[left] == DataType.BAD:
            now_sum -= customers[left]
        left += 1



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

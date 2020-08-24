
# 输入数组的大小和数组
# 输出这个数组的最大difference，要求被减数在减数的后面
# 如何确保被减数在减数的后面呢？
# for i 中的i对应的是被减数的位置，在每次完成减的操作以后，在i的前面找最小数
import sys
n = int(input())
array = list(map(int,input().split()))

def maxDifference(n,array):

    minElement = array[0]
    maxDifference = -sys.maxsize
    if n == 0:
        return None
    for i in range(1,n):
        maxDifference =max(maxDifference,array[i]-minElement)

        minElement = min(minElement,array[i])
    return maxDifference
print (maxDifference(n,array))

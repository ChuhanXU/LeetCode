
# 暴力解法是O(n^3)
# 可以一次找多个解，从而将时间复杂度变为O(n^3)
# sorted
# [1,2,3,4]
# 如果2+8大于2，说明3+8，4+8，5+8，6+8都大于2 一共有right(5)-left(0),批量累加，因为只要方案数
# https://www.jiuzhang.com/problem/triangle-count/
def triangleCount(array):

    ans = 0
    sortedArray = sorted(array)
    n = len(array)
    for i in range(n-1,1,-1):
        left = 0
        right = i-1
        while left<right:
            if sortedArray[left]+sortedArray[right]>sortedArray[i]:
                ans += right-left
                right-=1
            left+=1
    return ans
array = [2,4,5,6]
print(triangleCount(array))

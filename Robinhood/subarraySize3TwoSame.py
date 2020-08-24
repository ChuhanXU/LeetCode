
# 一个int array包含多少大小为3的子array满足相连三个元素中有且只有个两相同
# [1,2,2,1,2,3,2]
def twoSame(array):
    n = len(array)
    if n==0:
        return 0
    ans = 0
    for i in range(n-2):
        list = array[i:i+3]
        subarray = set(list)

        if len(subarray)==2:
            ans+=1


    return ans
array =[1,2,2,1,2,3,2]

print(twoSame(array))


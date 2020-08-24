
# input[3,3,5,2,1]
# output 3+2+1 =6
# 需要让数组里的每一个减第一个数，如果a[i]<a[0],则以当前位置为a[0]
# 开启下一轮，直到所有的元素都为0，记录所有减数的和
# [3,3,5,2,1]->[0,0,2,2,1]->[0,0,0,0,1]->[0,0,0,0,0]
# 3+2+1
# [3,2,5,2,1]->[0,2,5,2,1]->[0,0,3,0,1]->[0,0,0,0,1]
# 3+2+3+1
def inputsum(array):
    if len(array) == 0:
        return -1
    result = dfs(array,0)
    return result

def dfs(array,sum):
    n = len(array)
    for i in range(n):
        if array[i] != 0:
            num = array[i]
            sum+=num
            for j in range(n):
                if array[j]>=num:
                    array[j]-=num
        break

    return sum


print(inputsum([3,2,5,2,1]))




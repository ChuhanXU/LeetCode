
# input [25,35,872,228,53,278,872']
# output =4 (35,53) (872,278) (872',872),(278,872')

def digitNums(array):
    if len(array) == 0:
        return 0
    list = []
    for nums in array:
        numList = [int(x) for x in str(nums)]
        list.append(sorted(numList))
    n = len(list)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if list[i] == list[j]:
                ans += 1
    return ans

array = [25,35,872,228,53,278,872]
print(digitNums(array))


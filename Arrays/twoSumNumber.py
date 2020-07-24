# O(n2) O(1)
# def twoNumberSum(array, targetSum):
# 	for i in range(len(array)-1):
# 		firstNum=array[i]
# 		for j in range(i+1,len(array)):
# 			secondNum = array[j]
# 			if firstNum + secondNum == targetSum:
# 				return[firstNum,secondNum]
# 	return[]
# print(twoNumberSum([4, 7],10))
# O(n) O(n) n是字典nums的长度
# 遍历数组中的每个值，并算出相对应的potential值，如果potential值出现在数组中，则返回the pair of number,否则，put this number in the dic
def twoNumberSum(array, targetSum):
    nums = {}
    result = []
    if len(array) ==0 :
        return []

    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            result.append([potentialMatch, num])
        else:
            nums[num] = potentialMatch
    return result
# 双指针O(nlog(n)) O(1) 前提是排序
# def twoNumberSum(array, targetSum):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         # 		最小值加上最大值,using two pointers,on conditon that it is sorted
#         currentSum = array[left] + array[right]
#         if currentSum == targetSum:
#             return [array[left], array[right]]
#         elif currentSum < targetSum:
#             left += 1
#         elif currentSum > targetSum:
#             right -= 1
#     return []


print(twoNumberSum([4, 7, 6, 3], 10))

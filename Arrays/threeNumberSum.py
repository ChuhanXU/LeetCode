# def threeNumberSum(array, targetSum):
#     array.sort()
#     triplets = []
#     # 	for i in range(len(array)-2): array-2是因为指针指向的是i的右边的元素，要留一个出来
#     for i in range(len(array) - 2):
#         left = i + 1
#         right = len(array) - 1
#         while left < right:
#             currentSum = array[i] + array[left] + array[right]
#             if currentSum == targetSum:
#                 triplets.append([array[i], array[left], array[right]])
#                 # left += 1
#                 # right -= 1
#             elif currentSum < targetSum:
#                 left += 1
#             elif currentSum > targetSum:
#                 right -= 1
#     return triplets
def threeNumberSum(array, targetSum):
    array.sort()
    list = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if targetSum == currentSum:
                currentArray = [array[i], array[left], array[right]]
                list.append(currentArray)
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1

        # elif targetSum < currentSum:
        # 	right -=1
        # else:
        # 	left += 1
    return list

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],0))

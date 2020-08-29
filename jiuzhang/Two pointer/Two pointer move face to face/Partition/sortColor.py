

def sortColors(nums):
    # write your code here
    hash = {}
    n = len(nums)
    result = []
    for number in nums:
        hash[number] = hash.get(number, 0) + 1
    hash = sorted(hash.items(), key=lambda item: item[0])
    for num in hash:

        frequency = num[1]
        while frequency > 0:
            result.append(num[0])
            frequency -= 1
    return result
nums = [2,0,0,1,2,0,2]
print(sortColors(nums))
# def sortColors(self, nums):
#         # write your code here
#         if not nums:
#             return None
#         count_0, count_1, count_2 = 0, 0, 0
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 count_0 += 1
#             elif nums[i] == 1:
#                 count_1 += 1
#             elif nums[i] == 2:
#                 count_2 += 1
#         for a in range(count_0):
#             nums[a] = 0
#         for b in range(count_0, count_0+count_1):
#             nums[b] = 1
#         for c in range(count_0+count_1, len(nums)):
#             nums[c] = 2
# 1.一个hash 存上所有的数组中的值
# 2.遍历数组中的每一个元素，并在hash表中找到相邻的元素，如果已被找到，标记为false
# 时间复杂度是O(n)
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

def longestConsecutive(num):
    longestlength = 0
    hash = {}
    for number in num:
        hash[number] = True

    for number in num:
        if not hash[number]:
            continue

        hash[number] = False
        currentlength = 1
        left = number - 1
        right = number + 1
        while left in hash:
            hash[left] = False
            currentlength += 1
            left -= 1
        while right in hash:
            hash[right] = False
            currentlength += 1
            right += 1
        if currentlength > longestlength:
            longestlength = currentlength
    return longestlength
num = [3,2,7,5,6,6]
print(longestConsecutive(num))
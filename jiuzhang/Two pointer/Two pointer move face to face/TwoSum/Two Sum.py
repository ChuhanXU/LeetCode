
# 在未排序数组中，找到两个数和为target
# 哈希表做法 时间O(N) 空间O(n)
# we need to add number after target minus number
# for eample if we have a array like[2,4,8] and target = 8
# if we add first we will get a illegal result like[4,4]
class Solution:
    def twoSum(self,numbers,target):
        hashset = set()
        for number in numbers:
            if target - number in hashset:
                return number,target - number
            hashset.add(number)
        return [-1,-1]
# two pointer + sort
# time:O(nlogn) space:O(1)
# 大于排除最大的数，小于排除最小的数
#     follow up 如果输入数据已经排好序 O(n)O(1),双指针更好
#     如果要返回下标就要使用hash，因为排序会丢失index的信息
#

    def twoSum(self,numbers,target):
        if not numbers:
            return[-1,-1]
        # 如果想记录index的位置,二元组的排序先比较第一个再比较第二个
        # nums=[(number,index)for index,number in enumerate(numbers)]
        # nums.sort()
        # 带着index实现
        numbers = sorted(numbers)
        left,right = 0,len(numbers)-1
        while left < right:
            sum = numbers[left]+numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return numbers[left],numbers[right]
        return[-1,-1]



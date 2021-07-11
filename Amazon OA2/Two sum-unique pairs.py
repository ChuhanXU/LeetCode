
# Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target.
# Return the number of pairs.
def twoSum(nums, target):
    if not nums or len(nums) < 2:
        return 0

    nums.sort()

    count = 0
    left, right = 0, len(nums) - 1
    last_pair = (None, None)

    while left < right:
        if nums[left] + nums[right] == target:
            if (nums[left], nums[right]) != last_pair:
                count += 1
            last_pair = (nums[left], nums[right])
            left, right = left + 1, right - 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1

    return count
# nums = [1, 1, 2, 45, 46, 46]
# target = 47
# nums = [1, 1]
# target = 2
nums = [1, 5, 1, 5]
target = 6
print(twoSum(nums, target))
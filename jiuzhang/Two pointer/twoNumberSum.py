def twoNumberSum(nums,target):
    hash = {}
    n = len(nums)
    for i in range(n):
        potentialMatch = target - nums[i]
        if potentialMatch in hash:
            return(i,hash[potentialMatch])
        else:
            hash[nums[i]] = i
    return []

print (twoNumberSum([-12,13,14],1))
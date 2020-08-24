def twoNumberSum(nums,target):
    # {value:index}
    hash = {}
    n = len(nums)
    array=[]
    for i in range(n):
        potentialMatch = target - nums[i]
        if potentialMatch in hash:
            # 输出两个数的index
            # array.append([i,hash[potentialMatch]])
            # 输出两个数的值
            array.append([nums[i], potentialMatch])
        else:
            hash[nums[i]] = i
    for pair in array:
        pair[0],pair[1]=pair[1],pair[0]


    return array

print (twoNumberSum([0,-1,2,-3,4],1))
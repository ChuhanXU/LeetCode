def find_longest_consecutive_string(nums):
    if len(nums)==0:
        return 0
    visited = set()
    maxlength=0
    for num in nums:
        if num in visited:
            continue
        left = num-1
        right = num+1
        while left in nums:
            visited.add(left)
            left-=1
        while right in nums:
            visited.add(right)
            right+=1
        length = right-left-1
        maxlength = max(maxlength,length)
    return maxlength
nums=[2,99,1,3,4,100,5]
print(find_longest_consecutive_string(nums))




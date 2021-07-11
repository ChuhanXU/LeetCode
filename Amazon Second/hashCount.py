def count(nums):
    hash={}
    for num in nums:
        if num not in hash:
            hash[num]=1
        hash[num]+=1
    return hash
nums="aaabssbcbdb"
print(count(nums))
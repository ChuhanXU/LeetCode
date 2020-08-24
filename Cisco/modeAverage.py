
# 找平均数和众数
def modeMean(nums):
    count = [0]*(max(nums)+1)
    total = 0
    mode = 0
    for i in nums:
        count[i] += 1
        total += i
        if count[i] == mode:
            if i < mode:
                mode = i
        if count[i]>mode:
            mode = i
    avg = total/len(nums)
    return("{:.4f} {}".format(avg,mode))
nums = [1,2,3,2]
print(modeMean(nums))
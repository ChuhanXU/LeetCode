
# 找出数组中三个数相加为0的组合
# 假设a<=b<=c
# for 循环a 找b+c=-a 即可调用2 sum实现
# O(n^2)
# [-1,0,1,2,-1,-4]
# [-4,-1,-1,0,1,2]
# 固定第一个元素-1，在剩下的元素中找相加等于1的组合
def threeSum(nums):
    nums = sorted(nums)
    results = []
    for i in range (len(nums)):
        if i>0:
            continue
        # # if i>0 and nums[i]==nums[i-1]:
        #     continue
        find_two_sum(nums,i+1,len(nums)-1,-nums[i],results)
    return results


def find_two_sum(nums,left,right,target,results):
    last_pair = None
    while left < right:
        if nums[left]+nums[right]==target:
            if(nums[left],nums[right])!=last_pair:
                results.append([-target,nums[left],nums[right]])
            last_pair=(nums[left],nums[right])
            right-=1
            left+=1
        elif nums[left]+nums[right]>target:
            right-=1
        else:
            left+=1

numbers=[1,-1,-1,-1,2,2,2,-2,1]
print(threeSum(numbers))



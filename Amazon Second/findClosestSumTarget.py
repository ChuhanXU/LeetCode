
# what I am thinking is to use two pointers method to solve this problem,
# first I will sort each of these two arrays,because I want to make sure every time I move my
# pointer, I can get a closer sum to the target.
# my two pinter are left=0 for arrA, right =len(arrB)-1 for arrB
# if the absolute value of current difference is less than the previous smallest one
# I just update the smallest one with the current difference and the closest_pair
# if curren_diff==0: which means we find a pair which sum is exactly equal to the target
# then we just need to return this pair
# if current difference is less than 0 which means the sum is less than target,
# so in order to make it closer to the target, we need to make it bigger, so we just
# need to move our left point to the right, otherwise,if we want to get a smaller sum
# we move our right pointer to the left.until the one of pointers move to the beginning of
# array or the end of array

# corner case
# are you guaranteed these two array are not null
# if it is null what kind of data i should return

# what if we have two pairs which have same smallest absolute value of difference
# do i need to return all of them or just one of them

# time complexity
# because I used sort function, so it is nlogn

def closest_sum_pair(a1,a2,target):
    if len(a1)==0 or len(a2)==0:
        return -1
    a1_sorted = sorted(a1)
    a2_sorted = sorted(a2)
    result=[]
    left=0
    right = len(a2_sorted)-1
    smallest_diff = abs(a1_sorted[0]+a2_sorted[0]-target)
    closest_pair = (a1_sorted[0],a2_sorted[0])
    while left<=len(a1_sorted)-1 and right>=0:
        v1=a1_sorted[left]
        v2=a2_sorted[right]
        current_diff = v1+v2-target
        if abs(current_diff)<smallest_diff:
            smallest_diff=abs(current_diff)
            closest_pair=(v1,v2)
        if current_diff == 0:
            return closest_pair
        elif current_diff<0:
            left+=1
        else:
            right-=1
    return closest_pair
a1 = [-1, 3, 8, 2, 9, 5]
a2 = [4, 1, 2, 10, 5, 20]
a_target = 24
print(closest_sum_pair(a1,a2,a_target))







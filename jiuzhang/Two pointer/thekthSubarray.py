def thekthSubarray(num,k):
    n = len(num)
    left = 0
    right = 0
    # 二分法的划分的范围是 0 ~ sum(num)
    for i in range (n):
        right += num[i]

    while left+1 < right:
        mid = (left + right)//2
        if intervalNumber(num,mid)>=k:
            right = mid
        else:
            left = mid
    if intervalNumber(num, left) == k:
        return left
    return right
# 想办法得到当区间和<=x时的区间数量(总的子数组的数量减去大于x的子数组的数量)
def intervalNumber(num,x):
    n=len(num)
    res = 0
    start = 0
    end = 0
    sum = num[start]
    while start < n:
        # 不停的扩展,end,直到子数组的和大于x或者end到达边界
        while sum <= x:
            end += 1
            if(end >= n):
                break
            sum += num[end]
        if end < n:
            # end-1,end,end+1 ....n-1 满足和>x的子数组是从end开始的,因此是n-1-(end-1)
            res += n-end
        sum -= num[start]
        start += 1
    return (n+1)*n//2 - res
print(thekthSubarray([2,3,1,4],6))


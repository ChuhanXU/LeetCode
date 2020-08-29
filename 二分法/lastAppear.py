def lastappear(array,target):
    array = sorted(array)
    left,right = 0,len(array)-1

    while left+1<right:
        mid = (left + right) // 2
        if array[mid]>target:
            right = mid
        elif array[mid]<target:
            left = mid
        else:
            left = mid
    if array[right]==target:
        return right
    if array[left]==target:
        return left
array = [1,2,2,3,4]
print(lastappear(array,2))




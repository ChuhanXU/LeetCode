
#  we can use dichotomy twice,fist is to find the index of the min value in this array,second is to get the target value

def searchSortedArray(array,target):
    if not array:
        return -1
    index= findMinValue(array)

    if array[index]<=target<=array[-1]:
        return binarySearch(array,index,len(array)-1,target)

def findMinValue(array):
    left,right = 0, len(array)-1
    while left+1<right:
        mid = (left+right)//2
        if array[left]<array[right]:
            return array[left]
        else:
            if array[left]>array[mid]:
                right = mid
            elif array[left]<array[mid]:
                left = mid
            else:
                right = mid
    if array[left]<array[right]:
        return left
    return right
def binarySearch(array,start,end,target):
    while start+1<end:
        mid = (start+end)//2
        if array[mid]<target:
            start = mid
        elif array[mid]>target:
            end =mid
        else:
            end=mid
    if array[end]==target:
        return end
    if array[start]==target:
        return start
    return -1
array = [4,5,1,2,3]
print(searchSortedArray(array,3))



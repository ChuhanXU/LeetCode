def kClosestNumber(A,target,k):
    index = findIndex(A,target)
    left,right=index-1,index
    result = []
    for i in range(k):
        if left<0:
            result.append(A[right])
            right+=1
        elif right > len(A)-1:
            result.append(A[left])
            left-=1
        else:
            if target-A[left]<A[right]-target:
                result.append(A[left])
                left-=1
            else:
                result.append(A[right])
                right+=1
    return result

def findIndex(A,target):
    start,end = 0,len(A)-1
    while(start+1<end):
        mid = (start+end)//2
        if A[mid] < target:
            start = mid
        elif A[mid]> target:
            end = mid
        else:
            end=mid
    if A[start]>=target:
        return start
    if A[end]>=target:
        return end
    return len(A)
A=[1,3,7,8,5]
print(kClosestNumber(A,4,3))

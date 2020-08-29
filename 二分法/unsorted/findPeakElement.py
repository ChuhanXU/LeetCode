def findPeak(A):
    start,end = 1,len(A)-2
    while start<end:
        mid = (start+end)//2
        if A[mid]<A[mid-1]:
            end = mid
        elif A[mid]<A[mid+1]:
            start = mid
        else:
            return mid
    if A[start]>A[end]:
        return start
    return end
A=[1,2,4,2,1]
print(findPeak(A))
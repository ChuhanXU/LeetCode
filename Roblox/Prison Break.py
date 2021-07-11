def prisonbreak(m,n,h,v):
    res = helper(v)*helper(h)
    return res

def helper(array):
    array = sorted(array)
    count = 1
    maxnumber = 1
    for i in range(1,len(array),1):
        if array[i]==array[i-1]+1:
            count+=1
            maxnumber = max(maxnumber,count)
        else:
            count = 1
    return maxnumber+1

h = [1,2,3]
v = [2,1]
print(prisonbreak(6,6,h,v))
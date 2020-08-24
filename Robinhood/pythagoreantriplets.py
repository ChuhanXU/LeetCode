def pythagorean(array):
    n = len(array)
    ans= [0] *(n-2)
    for i in range(n-2):
        if (array[i]*array[i] + array[i+1]*array[i+1] == array[i+2]*array[i+2]):
            ans[i]=1
        if (array[i]*array[i] + array[i+2]*array[i+2] == array[i+1]*array[i+1]):
            ans[i]=1
        if (array[i+1]*array[i+1] + array[i+2]*array[i+2] == array[i]*array[i]):
            ans[i]=1
    return ans
array = [0,5,5,0,5,13,12]
print(pythagorean(array))

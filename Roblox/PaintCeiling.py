def variantsCount(n,s0,k,b,m,a):
    s = [0] * n
    s[0] = s0
    for i in range(1,n,1):
        s[i] = ((k*s[i-1]+b) % m)+1+s[i-1]
    count = 0
    i = 0
    j = n-1
    while i<=j:
        if s[i] * s[j] <= a:
            count += (((j-i) * 2)+1)
            i+=1
        else:
            j-=1
    return count

print(variantsCount(3,1,1,1,2,4))




import operator
def findAllTheWays(s,t):
    n=len(s)
    m=len(t)
    ans = 0
    for i in range(n):
        if s[i].isdigit():
            newS = s[0:i] + s[i+1:n]
            # operator.lt = less than
            if operator.lt(newS,t) :
                ans+=1
    for i in range(m):
        if t[i].isdigit():
            newT = t[0:i] + t[i+1:m]
            if operator.lt(s,newT) :
                ans+=1
    return ans
s="ab12c"
t="1zz456"
print(findAllTheWays(s,t))







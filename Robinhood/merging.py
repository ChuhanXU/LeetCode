def merge(s, t):
    n=len(s)
    m=len(t)
    if n==0:
        return t
    if m==0:
        return s
    string = ''
    a=min(n,m)
    for i in range(a):
        string += s[i]+t[i]
    if n-m>0:
        string+=string[-(n-m):]
    if m-n>0:
        string+=string[-(m-n):]
    return string
s='aaaaa'
t='bbb'
print(merge(s,t))
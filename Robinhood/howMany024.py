def howMany(n):
    ans = 0
    s=''
    for i in range(n+1):
        s += str(i)

    n = len(s)
    print(s)

    for i in range (n):
        if s[i]=='0':
            ans += 1
        elif s[i]=='2':
            ans += 1
        elif s[i]=='4':
            ans += 1
    return ans
print(howMany(22))

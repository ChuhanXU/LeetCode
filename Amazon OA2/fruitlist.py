def fruitlist(slist,purcharselist):
    if not slist:
        return True
    if not purcharselist:
        return False
    i,j=0,0
    while i<len(slist) and j+len(slist[i])<=len(purcharselist):
        answer = True
        for k in range(len(slist)):
            if slist[i][k]!='anything' and purcharselist[j+k]!=slist[i][k]:
                answer = False
                break
        if answer:
            j+=len(slist[i])
            i+=1
        else:
            j+=1
    if i==len(slist):
        return True
    else:
        return False
slist=[["watermelon","anything","mongo"]]
purcharselist=["watermelon","orange","mongo","apple"]
print(fruitlist(slist,purcharselist))




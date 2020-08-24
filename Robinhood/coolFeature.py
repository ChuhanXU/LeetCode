
# a=[1,2,3] b=[3,4]
# query = [[1,5],[0,0,1],[1,5]]
# output coolfeature(a,b,query) = [2,1]

# a=[1,2,2] b=[2,3] 换成 b=[3,3]
# query = [[1,4],[0,0,3],[1,5]]
# output coolfeature(a,b,query) = [3,4]

def coolfeature(a,b,querys):
    n= len(a)
    m = len(b)
    q=0
    ans = [0]*2
    for query in querys:
        if query[0]==1:
            ans[q]=operation1(a,b,n,m,query)
            q+=1
        if query[0]==0:
            b[query[1]]=query[2]
    return ans


def operation1(a,b,n,m,query):
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i] + b[j] == query[1]:
                ans += 1
    return ans
a=[1,2,2]
b=[2,3]
querys = [[1,4],[0,0,3],[1,5]]

print(coolfeature(a,b,querys))

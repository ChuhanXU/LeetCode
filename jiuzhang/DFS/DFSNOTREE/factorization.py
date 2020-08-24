
# 1000000以下的所有数字中，因子个数的数字大约有50-500个因子
# 30：2，3，5，6，10，15，1，30
# 每次放因子的时候保证下一个比上一个大
# 从 2 到 sqrt(x)+1可以找到所有的factor
# input:8
# output [[2,2,2],[2,4]]
import math


def getFactors(n):
    result = []
    path = []

    dfs(n,2,path,result)
    return result
def dfs(now_num,min_factor,path,result):
    if now_num == 1:
        # 防止结果里出现[8]
        if len(path) > 1:
            # 这里要进行一个深拷贝，因为后面会进行修改
            result.append(path[:])
        return
    # 尽量选择因子进行因式分解

    for i in range(min_factor,int(math.sqrt(now_num))+1):
        if now_num % i == 0:
            path.append(i)
            # i现在是min_factor
            dfs(now_num//i,i,path,result)
#             回溯
            path.pop()
#             还有种情况 8=2*4 也可以是8=2*2*2 我们呀需要把4塞进去
#     将数字不进行因式分解
    path.append(now_num)
    dfs(1,now_num,path,result)
    path.pop()
print(getFactors(30))

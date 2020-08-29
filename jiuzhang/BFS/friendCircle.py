
# https://www.jiuzhang.com/problem/friend-circles/
# 输入：[[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
# 解释：
# 0号和1号学生是直接朋友，所以他们位于一个朋友圈内。
# 2号学生自己位于一个朋友圈内。所以返回2.
# 输入：[[1,1,0],[1,1,1],[0,1,1]]
# 输出：1
# 解释：
# 0号和1号学生是直接朋友，1号和2号学生处于同一个朋友圈。
# 所以0号和2号是间接朋友。所有人都处于一个朋友圈内，所以返回1。
#   0 1 2 3
# 0 1 0 0 1
# 1 0 1 1 0
# 2 0 1 1 1
# 3 1 0 1 1
import collections


def findCircle(M):
    n = len(M)
    visited = {}
    ans =0
    for i in range(n):
        visited[i]=False
    for i in range(n):
        if visited[i] == False:
            ans+=1
            queue=collections.deque()
            queue.append(i)
            visited[i]=True
            while queue:
                now = queue.popleft()
                for j in range(n):
                    if M[now][j]==1 and visited[j]==False:
                        queue.append(j)
                        visited[j]=True
    return ans
M=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(findCircle(M))
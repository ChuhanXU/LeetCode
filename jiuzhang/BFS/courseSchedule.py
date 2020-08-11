
# 拓扑排序加BFS
# 如果不建图的时间复杂度是O(VE)，建图的时间复杂度是O(V+E)


# 1. 如果课程的数量为0，则返回空数组
# 2. 因为如果我们直接通过遍历prerequisites来查询不同课程的先行课程，时间复杂度会很高，因此考虑建图
# ps:什么时候考虑建图，如果无法在O(1)的时间找不到相邻的点
# 3. 用一个类似哈希的结构记录每门课的后行课，同时用一个indegrees来记录每门课的度
# 4.将没门课的后行课放到对应课的set中，如果这门课中还没有这个后行课

# do we have completely same pair in the prerequisites, no
# so we don't need to worry we will put one prerequisite twice for certain course

# if the number of course is zero, what result we should return a empty array or -1

# I will use topological sort to finish this problem, the time complexity will be o(v+e), go back to this question, the v will be the number of node


import collections


def findOrder(numCourses,prerequisites):
    if numCourses == 0:
        return []

    # 入度
    indegrees = [0] * numCourses
    # [n,p]要上1必须先上0
    # prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]] n = 4
    # 建图调整数据结构[0:{1,2},1:{3},2:{3},3:{}]
    # indegrees[0,1,1,2]

    edges = {i:set() for i in range(numCourses)}
    for n,p in prerequisites:
        if n not in edges[p]:
            indegrees[n]+=1
            edges[p].add(n)


    queue = collections.deque()
    # 将入度为0的放入队列,入度为0说明没有先修课，第一个放入队列的是0
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)

    order = []

    while queue:
        now = queue.popleft()
        order.append(now)
        for next_point in edges[now]:
            indegrees[next_point] -= 1
            if indegrees[next_point] == 0:
                queue.append(next_point)

    if len(order) != numCourses:
        return[]

    return order



print(findOrder(4,[[1, 0], [2, 0], [3, 1], [3, 2]]))




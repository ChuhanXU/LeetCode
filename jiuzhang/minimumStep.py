# colors = [1, 2, 3, 3, 2, 5]
# color_group[[],[0],[1,4],[2,3],[],[5],[]]，颜色3的坐标为2，3 color_group[颜色]=一个数组(所有此颜色的位置)
# 1.将节点按颜色分组到二维数组colorGroup中
# 2.新建一个队列，将节点0加入到队列中，且更新节点0的状态
# 3.取出队首节点pos，代表当前搜索的位置
# 4.将未访问过的同颜色节点加入队列，并更新状态
# 5.将左右两个位置为访问过的节点加入队列，并更新状态
# 6.如果队列中还有元素，回到第三步，直到队列是空的为止
# 7.返回节点n-1的最短路
import collections
def minimumStep(colors):
    n = len(colors)
    # 记录最小的步数
    min_step = {}
    # 记录被访问过的位置
    visited_grid = set()
    # 记录被访问过的颜色
    visited_color = set()

    # 按颜色分类
    color_group = [[]for _ in range(n+1)]
    for i in range(n):
        color_group[colors[i]].append(i)
#     新建一个队列
    que = collections.deque()
    que.append(0)
    min_step[0] = 0
    visited_grid.add(0)

    while que:
        pos = que.popleft()
        # 拿到起始点的颜色为1
        color = colors[pos]
#         如果某个颜色未处理过，先处理这个颜色
        if color not in visited_color:
            visited_color.add(color)
#             将未访问过的同颜色的节点加入队列并更新状态
#             遍历color_group中对应颜色的位置，通过isValid的判断是否可以将此同颜色的节点放入队列
            for newPos in color_group[color]:
                if isValid(n,newPos,visited_grid):
                    min_step[newPos] = min_step[pos]+1
                    que.append(newPos)
                    visited_grid.add(newPos)
        # 将左右两个位置为访问过的节点加入队列，并更新状态
        newPos = pos + 1
        if isValid(n,newPos,visited_grid):
            min_step[newPos] = min_step[pos]+1
            que.append(newPos)
            visited_grid.add(newPos)
        newPos = pos -1
        if isValid(n,newPos,visited_grid):
            min_step[newPos] = min_step[pos] + 1
            que.append(newPos)
            visited_grid.add(newPos)
    return min_step[n-1]
def isValid(n,position,visited_grid):
    if position < 0 or position >= n:
        return False
    if position in visited_grid:
        return False
    return True

print(minimumStep([1, 2, 3, 3, 2, 5]))





import collections
class DataType:
    ROAD = 0
    WALL = 1
    DESTINATION = 2
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]


# 初始化队列(一个空队列和哪些点被访问过了)
# 把起始点加入队列
# BFS
# 只要队列非空
#   把当前队列的所有元素取出来
#   if是否当前位置是终点
#       返回走的步数
#   for周围的点
#       if 能加入队列
#           加入队列
#   走的步数 += 1
# 哪些数据结构可以用来存储被访问过的节点(二维数组bool, set()/hashmap),统一用set()和hashmap
def shortestPath(self,targetMap):
    n= len(targetMap)
    if n == 0:
        return 0
    m = len(targetMap[0])
    if m == 0:
        return 0
    queue = collections.deque()
    # set 的意义在于判断是否有条件元素在set中
    visited = set()
    steps = 0
    # 在bfs里这两个是同时出现的
    queue.append((0,0))
    visited.add((0,0))

    while queue:
        for _ in range(len(queue)):
            x,y = queue.popleft()
            if targetMap[x][y] == DataType.DESTINATION:
                return steps
            for delta_x, delta_y in DIRECTIONS:
                next_x = x+delta_x
                next_y = y + delta_y
                if is_valid(next_x,next_y,targetMap,visited):
                    queue.append(next_x,next_y)
                    visited.add(next_x,next_y)
        steps += 1
    return -1
def is_valid (x,y,targetMap,visited):
    if x<0 or y<0 or x>=len(targetMap) or y>=len(targetMap[0]):
        return False
    if targetMap[x][y]==DataType.Wall:
        return False
    if(x,y)in visited:
        return False
    return True






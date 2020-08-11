
# 不能从所有的房子开始bfs
# 从某个房子bfs 对所有房子做一遍bfs
# 1.怎么知道每个空地离所有房子的总距离？
# push model: 每个房子bfs到某个空地 distance[空地]  += 当前距离
# 2.如何判断这个空地可以到达所有的房子
# reachable_building_number += 1

# 预先知道的东西 total_building distance[空地] 每个空地到所有房子的距离
# reachable_building_number 每个空地可以到达的房子的数量
import collections
import sys


class DataType:
    EMPTY = 0
    HOUSE = 1
    WALL = 2
DIRECTIONS=[(0,-1),(0,1),(-1,0),(1,0)]

def shorttestDistance(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return -1

    n,m = len(grid),len(grid[0])
        # 使用二维数组来储存需要更新的distance 和 reachable_number
    distance = [[0 for j in range(m)] for i in range(n)]
    reachable_number = [[0 for j in range(m)] for i in range(n)]

    total_building = 0
    min_distance = sys.maxsize
        # 计算出这一区房子的数量
    for i in range(n):
        for j in range(m):
            if grid[i][j] == DataType.HOUSE:
                bfs(grid, i, j, distance, reachable_number)
                total_building += 1
        # 主函数，对房子进行bfs
    for i in range(n):
        for j in range(m):
            # 找到空地,并更新二维数组中对应的reachable_number和 distance
            if grid[i][j] != DataType.EMPTY:
                continue
            if reachable_number[i][j] != total_building:
                continue

            min_distance = min(min_distance,distance[i][j])

    if min_distance == sys.maxsize:
        return -1
    return min_distance

def bfs(grid,x,y,distance, reachable_number):
    visited = set([(x,y)])
    queue = collections.deque([(x,y,0)])

    while queue:
        x, y,current_distance = queue.popleft()
        distance[x][y] += current_distance
        reachable_number[x][y] +=1

        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if is_valid(grid, next_x, next_y, visited):
                queue.append((next_x, next_y,current_distance+1))
                visited.add((next_x, next_y))



def is_valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if (x, y) in visited:
        return False
    if grid[x][y] != DataType.EMPTY:
        return False
    return True

grid = [[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]

print(shorttestDistance(grid))
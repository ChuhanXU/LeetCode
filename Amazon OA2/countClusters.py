import collections
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 1.遍历整个矩阵，对矩阵中没有visited的点进行BFS
# 2.遍历四个方向，判断是否可以加入队列
# 3，先判断点是否可以加入队列的函数
def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    characterList=['a','b','c']
    cluster = 0
    visited = set()
    queue = collections.deque()
    for item in characterList:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==item and (i, j) not in visited:
                    bfs(grid, i, j, queue,visited,item)
                    cluster += 1
    return cluster


def bfs(grid, x, y,queue, visited,item):
    # 队列里放的是坐标，但是要以list的形式放进去
    queue.append((x, y))
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if is_valid(grid, next_x, next_y, visited,item):
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))


def is_valid(grid, x, y, visited,item):
    n, m = len(grid), len(grid[0])
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if (x, y) in visited:
        return False
    if grid[x][y] != item:
        return False
    return True
matrix = [
  ['a','a','b','b','a'],
  ['a','a','b','b','a'],
  ['a','a','a','c','b']

]
print(numIslands(matrix))
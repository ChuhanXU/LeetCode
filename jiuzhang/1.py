# 只有找到1了才放入队列，如果队列为空了还没有找到1的点，就返回上一级，岛屿数量+1
import collections
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def numIslands( grid):
    if not grid or not grid[0]:
        return 0

    islands = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] and (i, j) not in visited:
                bfs(grid, i, j, visited)
                islands += 1

    return islands


def bfs(grid, x, y, visited):
    queue = collections.deque([(x, y)])
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if not is_valid(grid, next_x, next_y, visited):
                continue
            queue.append((next_x, next_y))
            visited.add((next_x, next_y))


def is_valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if not (0 <= x < n and 0 <= y < m):
        return False
    if (x, y) in visited:
        return False
    if grid[x][y] == 0:
        return False
    return True
matrix = [
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
print(numIslands(matrix))
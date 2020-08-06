import collections
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 1.遍历整个矩阵，对矩阵中没有visited的点进行BFS
# 2.遍历四个方向，判断是否可以加入队列
# 3，先判断点是否可以加入队列的函数
def numIslands(grid,k):
    if not grid or not grid[0]:
        return 0

    islands = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1 and (i, j) not in visited:

                if bfs(grid, i, j, visited) >= k:
                    islands += 1

    return islands


def bfs(grid, x, y, visited):
    count = 0
    # 如果没有中括号，队列里会有x，y两个元素
    queue = collections.deque([(x, y)])
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()
        count += 1
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if is_valid(grid, next_x, next_y, visited):
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
    return count



def is_valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if x<0 or y<0 or x>=n or y>=m:
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
print(numIslands(matrix,2))
# O(KNM)k是查询次数
import collections
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]

def numIslands2(n,m,operators):
    if n == 0 or m == 0:
        return -1
    grid = [[0 for j in range(m)] for i in range(n)]


    # 用一个set记录访问过的点

    result = []
    for x,y in operators:
        grid[x][y]=1
        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i, j) not in visited:
                    bfs(grid, i, j, visited)
                    islands += 1
        result.append(islands)
    return result


def bfs(grid, x, y, visited):

    # 如果没有中括号，队列里会有x，y两个元素
    # 如果写成((x, y)),队列会认为你有两个元素
    queue = collections.deque([(x, y)])
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()

        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if is_valid(grid, next_x, next_y, visited):
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))




def is_valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if (x, y) in visited:
        return False
    if grid[x][y] == 0:
        return False
    return True
operators = [[1,1],[0,1],[3,3],[3,4]]
print(numIslands2(4,5,operators))
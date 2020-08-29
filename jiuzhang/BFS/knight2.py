import collections

directions = [(1, 2), (-1, 2), (2, 1), (-2, 1)]


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

def shortestPath2(grid):
    n=len(grid)
    m=len(grid[0])
    if n == 0:
        return -1
    if m == 0:
        return -1

    queue = collections.deque()
    dist = {}
    queue.append((0, 0))
    dist[(0, 0)] = 1
    while queue:
        x, y = queue.popleft()
        for del_x, del_y in directions:
            next_x = x + del_x
            next_y = y + del_y
            if is_valid(grid, next_x, next_y, dist):
                queue.append((next_x, next_y))
                dist[(next_x, next_y)] = dist[(x, y)] + 1

    if (n - 1, m - 1) not in dist:
        return -1
    return dist[(n - 1, m - 1)]

def is_valid(grid, x, y, dist):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False
    if (x, y) in dist:
        return False
    if grid[x][y] == 1:
        return False
    return True
grid = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]
print(shortestPath2(grid))
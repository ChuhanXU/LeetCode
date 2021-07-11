import collections
# 用一个hashtable来存储步数

DIRECTIONS = [(-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2)]
def shortestPath(grid,visited,source,destination):
    queue = collections.deque([(source[0], source[1])])
    hashtable = {(source[0], source[1]): 0}
    visited.add((source[0], source[1]))
    while queue:
        x, y = queue.popleft()
        # if(x,y)== (destination[0],destination[1]):
        #     return hashtable[(x,y)]
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if is_valid(grid, next_x, next_y, visited):
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                hashtable[(next_x, next_y)] = hashtable[(x, y)] + 1
    if (destination[0],destination[1]) not in hashtable:
        return -1
    return hashtable[(destination[0],destination[1])]


def is_valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if not (0 <= x < n and 0 <= y < m):
        return False
    if (x, y) in visited:
        return False
    if grid[x][y] == 1:
        return False
    return True
matrix = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]
visited = set()
source = [0,0]
destination = [2,2]
print(shortestPath(matrix,visited,source,destination))
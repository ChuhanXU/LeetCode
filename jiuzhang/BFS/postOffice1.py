
# 可以问面试官的问题，在这个地方是空地多还是房子多
# 方法一:bfs每个空地，算出每个空地到所有房子的距离，然后选出最小值，在空地较少的情况下可以使用该方法
# 方法二:bfs每个房子，不是把所有的房子都放入队列，而是一个个的bfs，把每一个house到空地的距离加起来，取最小值
# 方法一，从bfs空地
import collections
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def postOffice(grid):

    if len(grid)==0 or len(grid[0]) == 0:
        return -1

    n, m = len(grid), len(grid[0])
    visited=set()
    distance = [[None for _ in range(m)] for _ in range(n)]
    house_number = count_house(grid)


    for i in range(n):
        for j in range(m):

            if grid[i][j] != 0:
                continue
                # 如果是空地，bfs
            bfs(grid, i, j, distance,visited,house_number)
    ans = float('inf')
    # 打擂台
    for i in range(n):
        for j in range(m):
            if distance[i][j] is not None and distance[i][j] < ans:
                # 所有房子到这块空地的距离
                ans = distance[i][j]
    # 如果有更新，说明有空地可以到达所有的房子，没有则说明没有空地满足条件
    if ans < float('inf'):
        return ans
    return -1


def count_house(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
    return count

def bfs(grid,x,y,distance,visited,house_number):
    queue = collections.deque([(x, y,0)])
    visited.add((x, y))
    house_count = 0
    sum_distance = 0
    while queue:
        x, y,current_distance = queue.popleft()
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if is_valid(grid, next_x, next_y, visited):
                queue.append((next_x, next_y,current_distance+1))
                visited.add((next_x, next_y))
                if grid[next_x][next_y] == 1:
                    house_count+=1
                    sum_distance+=current_distance+1
    if house_count == house_number:
        distance[x][y] = sum_distance


def is_valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if (x, y) in visited:
        return False
    if grid[x][y] != 0:
        return False
    return True
print(postOffice([[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]))


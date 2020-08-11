
# 僵尸矩阵
# Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).
# Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall.
# How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.
# 分层BFS，需要最少天完成这个东西 或者求最短路径问题
# 如果分层的话，我需要一个东西来确定这层的东西是否用完，然后来判断几层
# 因此我们把tuple设置成这样(x,y,now_days)，就不用确定每个人在第几天被感染
import collections
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def zombie(grid):

    if len(grid)==0 or len(grid[0]) == 0:
        return -1

    n,m = len(grid),len(grid[0])
    queue = collections.deque()
    visited = set()
    human_number = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 :
                human_number+=1

            #和大岛的问题不一样，这里需要把所有的僵尸放入队列，然后BFS
            if grid[i][j] == 1 :
                queue.append((i, j, 0))
                visited.add((i,j))
    ans = 0


    while queue:
        x,y,now_day = queue.popleft()
        ans = max(ans,now_day)
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if is_valid(grid, next_x, next_y, visited):
                queue.append((next_x, next_y,now_day+1))
                visited.add((next_x, next_y))
                human_number -= 1
    if human_number == 0:
        return ans
    return -1


def is_valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if (x, y) in visited:
        return False
    if grid[x][y] != 0:
        return False
    return True

grid=[[0,1,2,0,0],
      [1,0,0,2,1],
      [0,1,0,0,0]
      ]
print(zombie(grid))




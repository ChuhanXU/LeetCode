import collections
DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]

def numberOfIslands(matrix):
    if not matrix:
        return 0
    queue = collections.deque()
    visited = set()
    island = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1 and (i,j) not in visited:
                bfs(matrix,i,j,queue,visited)
                island+=1
    return island

def bfs(matrix,x,y,queue,visited):
    queue.append((x,y))
    visited.add((x,y))

    while queue:
        x,y = queue.popleft()
        for delta_x,delta_y in DIRECTIONS:
            next_x = x+delta_x
            next_y = y+delta_y
            if is_valid(matrix,next_x,next_y,visited):
                queue.append((next_x,next_y))
                visited.add((next_x,next_y))

def is_valid(matrix,x,y,visited):
    if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0]):
        return False
    if (x,y) in visited:
        return False
    if matrix[x][y]==0:
        return False
    return True

matrix = [
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
print(numberOfIslands(matrix))

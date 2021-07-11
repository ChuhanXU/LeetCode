import collections
class DataType:
    Directions=[(0,1),(0,-1),(1,0),(-1,0)]
def path(size,location):
    a = size[0]
    b = size[1]
    locker = 1
    matrix = [[0 for i in range(b)] for i in range(a)]
    result = [[0 for i in range(b)] for i in range(a)]
    matrix[location[0]][location[1]]=locker
    for i in range(a):
        for j in range(b):
            ans = bfs(i,j,locker,matrix)
            result[i][j]=ans
    return result
def bfs(x,y,locker,matrix):
    queue = collections.deque()
    visited = set()
    queue.append((x,y))
    visited.add((x,y))
    step =0
    while queue:
        for _ in range(len(queue)):
            x,y=queue.popleft()
            if matrix[x][y] == locker:
                return step
            for x_delta,y_delta in DataType.Directions:
                x_next = x+x_delta
                y_next = y+y_delta
                if is_valid (x_next,y_next,matrix,visited):
                    queue.append((x_next,y_next))
                    visited.add((x_next,y_next))
        step+=1
    return -1
def is_valid(x,y,matrix,visited):
    if x<0 or y<0 or x>=len(matrix)or y>=len(matrix[0]):
        return False
    if (x,y) in visited:
        return False
    return True


size=(3,3)
location = (1,1)

print(path(size,location))

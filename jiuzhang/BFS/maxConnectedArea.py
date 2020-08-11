
# 可以直接用hash table 解决
# 我们可以先通过bfs的做法，来直接看一下每个岛屿的大小，bfs返回的直接是面积，这一块其实就是在求大岛的面积，但是需要用hash记录一下每个编号岛屿的面积
# 然后枚举 0 所在的位置，把0变成1，看周围和几个相连即可。
# 注意的点我们需要record the maximum area of these connected area for the all of them. then compare it to the area after changed 0 to 1
import collections

DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def maxArea(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # 存放已访问过的位置
    visited = set()
    # 存放每个位置的连通块编号值
    # {(0,1):1,(1,0):2}
    position_index = {}
    # 存放每个编号的连通块面积
    # {1:1,2:1}
    size_for_index = {}

    index = 0
    maximum_area = 0

    # 宽度优先搜索，对是1的位置的连通块编号
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 1 and (x, y) not in visited:
                # 看队列会空几次，每空一次说明找到了一个完整的大岛，周围都是海，给每个岛编号
                index += 1
                area = bfs(x, y, n, m, visited, position_index, matrix, index)
                maximum_area = max(maximum_area, area)
                size_for_index[index] = area

    visited = set()

    # 检查每个是0的位置，计算出将它变为1的面积
    for x in range(n):
        for y in range(m):
            # 遍历所有的0，check if there is a island on its neighbors,if yes,record the index of this neighbor by checking on position_index hash table
            if matrix[x][y] == 0:
                neighbors_index = set()
                for direction in DIRECTIONS:
                    neighbor = (x + direction[0], y + direction[1])
                    if valid(neighbor, n, m, visited, matrix):
                        neighbors_index.add(position_index[neighbor])
                area = 1
                for index in neighbors_index:
                    area += size_for_index[index]
                maximum_area = max(maximum_area, area)

    return maximum_area

def bfs(x, y, n, m, visited, position_index, matrix, index):
    queue = collections.deque()

    queue.append((x, y))
    area = 0
    position_index[(x, y)] = index
    visited.add((x, y))

    while queue:
        (x, y) = queue.popleft()
        area += 1
        for direction in DIRECTIONS:
            new_position = (x + direction[0], y + direction[1])
            if valid(new_position, n, m, visited, matrix):
                queue.append(new_position)
                visited.add(new_position)
                position_index[new_position] = index
    return area

# 检查下一位置是否合法
def valid(position, n, m, visited, matrix):
    (x, y) = position
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if matrix[x][y] == 0:
        return False
    if (x, y) in visited:
        return False
    return True

print(maxArea([[0,1]
,[1,0]]))
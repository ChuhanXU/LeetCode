# 树上最长路径BFS
# 第一次BFS：从任意点(root)开始，找到起点(start),离root最远的点
# 第二次BFS：从起点开始，找到终点(end),离start最远的点
# 起点到终点就是最长路径
import collections


def longestPath(n, starts, ends, lens):
    neighbors = {}
    for i in range(n - 1):
        start = starts[i]
        end = ends[i]
        dist = lens[i]
        # 因为图是无向的，因此要建来回的边在两个结点之间
        if start not in neighbors:
            neighbors[start] = []
        if end not in neighbors:
            neighbors[end] = []

        neighbors[start].append((end, dist))
        neighbors[end].append((start, dist))
    # return:离root最远的点，该点离root的距离,start 是离root最远的点，root可以任意选择，
    start, _ = bfs(0, neighbors)
    end, answer = bfs(start, neighbors)
    return answer


def bfs(root, neighbors):
    queue = collections.deque()
    distance_to_root = {}

    queue.append(root)
    distance_to_root[root] = 0

    maximum_distance = 0
    maximum_node = -1

    while queue:
        now = queue.popleft()

        if maximum_distance < distance_to_root[now]:
            maximum_distance = distance_to_root[now]
            maximum_node = now

        for neighbor, edge_length in neighbors[now]:
            if neighbor in distance_to_root:
                continue

            queue.append(neighbor)
            distance_to_root[neighbor] = distance_to_root[now] + edge_length
    return (maximum_node, maximum_distance)
starts =[0,0,2,2]
ends = [1,2,3,4]
lens = [1,2,5,6]

print(longestPath(5, starts, ends, lens))

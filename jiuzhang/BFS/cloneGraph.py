# 克隆一张无向图. 无向图的每个节点包含一个 label 和一个列表 neighbors. 保证每个节点的 label 互不相同.
#
# 你的程序需要返回一个经过深度拷贝的新图. 新图和原图具有同样的结构, 并且对新图的任何改动不会对原图造成任何影响.
import collections

#
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self,node):
        root = node
        if node is None:
            return node
    # step1: use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getNodes(node)

    # step2: copy nodes,store the old-> new mapping information in a hash map
    # A->A',B->B'
        hash = {}
        for node in nodes:
            hash[node] = UndirectedGraphNode(node.label)
    #  step3: copy edges
        for node in nodes:
            new_node = hash[node]
            for neighbor in node.neighbors:
                new_neighbor = hash[neighbor]
                new_node.neighbors.append(new_neighbor)
        return hash[root]



    def getNodes(self,node):
        queue= collections.deque([node])
        visited = set([node])
        while queue:
            currentNode = queue.popleft()
            for neighbor in currentNode.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return visited

import heapq
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        graph = self.build_graph(words)
        if not graph:
            return ""
        return self.topological_sort(graph)

    def build_graph(self, words):
        # key is node, value is neighbors
        graph = {}

        # initialize graph
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

                    # add edges
        n = len(words)
        # we don't need to compare the last word to another word
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                #     这一块在干嘛？
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return None

        return graph

    def topological_sort(self, graph):
        # initialize indegree
        indegree = {
            node: 0
            for node in graph
        }

        # calculate indegree
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] = indegree[neighbor] + 1

        # use heapq instead of regular queue so that we can get the
        # smallest lexicographical order
        queue = [node for node in graph if indegree[node] == 0]
        heapq.heapify(queue)

        # regular bfs algorithm to do topological sorting
        topo_order = ""
        while queue:
            node = heapq.heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heapq.heappush(queue, neighbor)

        # if all nodes popped
        if len(topo_order) == len(graph):
            return topo_order

        return ""

solution = Solution()
["ze","yf","xd","wd","vd","ua","tt","sz","rd", "qd","pz","op","nw","mt","ln","ko","jm","il", "ho","gk","fa","ed","dg","ct","bb","ba"]
words = ["wrt","wrf","er","ett","rftt"]
print(solution.alienOrder(words))
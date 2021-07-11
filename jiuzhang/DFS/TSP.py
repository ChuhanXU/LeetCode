# 给 n 个城市(从 1 到 n)，城市和无向道路成本之间的关系为3元组 [A, B, C]（在城市 A 和城市 B 之间有一条路，成本是 C）
# 我们需要从1开始找到的旅行所有城市的付出最小的成本。
# Example 1
#
# Input:
# n = 3
# tuple = [[1,2,1],[2,3,2],[1,3,3]]
# Output: 3
# Explanation: The shortest path is 1->2->3
# 建图
# {1: {1: inf, 2: 1, 3: 3}, 2: {1: 1, 2: inf, 3: 2}, 3: {1: 3, 2: 2, 3: inf}}
class Result:
    def __init__(self):
        self.min_cost = float('inf')
class Solution:
    def minCost(self,n,roads):
        graph = self.construct_graph(roads,n)
        result = Result()
        self.dfs(1,n,set([1]),0,graph,result)
        return result.min_cost

    def dfs(self,city,n,visited,cost,graph,result):
        if len(visited)==n:
            result.min_cost = min(result.min_cost,cost)
            return
        for next_city in graph[city]:
            if next_city in visited:
                continue
            cost += graph[city][next_city]
            visited.add(next_city)
            self.dfs(next_city,n,visited,cost,graph,result)
            visited.remove(next_city)

    def construct_graph(self,roads,n):
        # i(city node):{1:inf,2:inf,3:inf} i到各个城市的点的距离
        graph = {
            i:{j:float('inf') for j in range(1,n+1)}
            for i in range(1,n+1)
        }
        for a,b,c in roads:
            graph[a][b]=min(graph[a][b],c)
            graph[b][a]=min(graph[b][a],c)
        return graph

roads = [[1,2,1],[2,3,2],[1,3,3]]
solution = Solution()
print(solution.minCost(3,roads))
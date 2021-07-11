# traverse to figure out if it's a connect G.
# You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.
#
# Input:
# The input to the function/method consists of three arguments:
#
# numNodes, an integer representing the number of nodes in the graph.
# numEdges, an integer representing the number of edges in the graph.
# edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
# Output:
# Return a list of integers representing the critical nodes.
#
# Example:
#
# Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
def traverse(eg, l, r):#[1,3] e[0]=1 e[1]=3 l=1 r=3
    tmpA = set()
    for e in eg:
        if e == [l, r]:
            continue
        elif len(e) == 2:# [2,3] tmp.add(2)
            if e[0] == l:
                tmpA.add(e[1])
            elif e[0] == r:
                tmpA.add(e[1])
            elif e[1] == l:
                tmpA.add(e[0])
            elif e[1] == r:
                tmpA.add(e[0])
    return tmpA


def solution(numNodes, numEdges, edges):
    # list for answer
    ans = []

    # get every node
    a = set()
    for e in edges:
        for i in e:
            a.add(i)

    # brute force method
    # loop thru unique node
    for i in a:
        # a graph from which i is removed
        newL = []
        for e in edges:
            tmp = []
            for j in e:
                if j != i:
                    # edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
                    tmp.append(j)
            newL.append(tmp)
        print(i, "has been removed->", newL)
        # tmp set for checking if the graph is connected
        tt = set()
        # add i for the if condition below
        tt.add(i)
        # find a connected graph
        for e in newL:
            if len(e) == 2:
                tmpSet = (traverse(newL, e[0], e[1]))
                tt = tt.union(tmpSet)
        print(tt, "<->", a)
        if bool(a.difference(tt)):
            ans.append(i)
        print("=" * 8)
    print("Answer: {}".format(ans))
    return ans


numNodes = 7
numEdges = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
solution(numNodes, numEdges, edges)

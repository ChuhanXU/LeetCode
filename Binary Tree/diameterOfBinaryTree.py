# 求二叉树的直径，一般会用到递归和分治，把大问题化成小问题，分别去看root.right,root.left
# 求二叉树中的求路径一般有两种情况，不过根结点，max(left chain,right chain)过根结点max(left_path,left_path,left chain + right chain)
# 在求chain的时候要需要考虑此节点的上一个路径，因为我们需要满足left chain + right chain等于根结点分别到左右节点的那个距离
import collections


def diameterOfBinaryTree(tree):
    longest,diameter = helper(tree)
    return diameter

def helper(tree):
    if tree is None:
        return 0,0
    left_longest, left_diameter = helper(tree.left)
    right_longest, right_diameter = helper(tree.right)

    longest = max(left_longest,right_longest)+1
    diameter = max (left_diameter,right_diameter,left_longest+right_longest)

    return longest,diameter

# 树上最长路径，需要建图dfs
def longestPath(n,starts,ends,lens):
    neighbors = {}
    for i in range(n-1):
        start = starts[i]
        end = ends[i]
        dist = lens[i]
        # 因为图是无向的，因此要建来回的边在两个结点之间
        if start not in neighbors:
            neighbors[start] = []
        if end not in neighbors:
            neighbors[end] = []

        neighbors[start].append((end,dist))
        neighbors[end].append((start,dist))
    # 这个0可以是起点，没有父亲节点 为-1
    chain,path = dfs(0,-1,neighbors)
    return path
def dfs(root,parent,neighbors):
    # 定义dfs，这里递归没写出口，因为我们没有指向null的一条边，当for循环执行完，也就自然遍历了所有的边
    longest_chain = 0
    longest_path = 0

    child_longest_chain = 0
    child_second_longest_chain = 0

    for neighbor,dist in neighbors[root]:
        if neighbor == parent:
            continue
        #     加dist是因为需要使left chain + right chain 等于过节点的最大链
        child_chain,child_path = dfs(neighbor,root,neighbors)
        child_chain += dist

        longest_path=max(child_path,longest_path)
        longest_chain=max(child_chain,longest_chain)

        _,child_second_longest_chain,child_longest_chain=sorted([child_chain,child_second_longest_chain,child_longest_chain])

        longest_path=max(child_second_longest_chain+child_longest_chain,longest_path)

    return[longest_chain,longest_path]

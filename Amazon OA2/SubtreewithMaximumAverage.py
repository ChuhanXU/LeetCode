class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maximumAverageSubtree(self, root):
        self.dic = {}
        self.inordersum(root)
        return max(self.dic.items(), key=lambda x: x[1])[0]
    # dfs
    def inordersum(self, root):
        if root:
            total = root.val
            nodeCount = 1

            for child in root.children:
                childSum, childCount = self.inordersum(child)
                total += childSum
                nodeCount += childCount

            avg = (total) / (nodeCount)

            if nodeCount != 1:
                self.dic[root.val] = avg
            return [total, nodeCount]
        else:
            return [0, 0]


n4 = TreeNode(110, [])
n5 = TreeNode(20, [])
n6 = TreeNode(30, [])
n7 = TreeNode(150, [])
n8 = TreeNode(80, [])
n2 = TreeNode(120, [n4, n5, n6])
n3 = TreeNode(180, [n7, n8])
n1 = TreeNode(200, [n2, n3])
ss = Solution()
print(ss.maximumAverageSubtree(n1))



class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(tree, subtree):
    if not subtree:
        return True
    return dfs(tree, subtree)

def checkTree(root1, root2):
    if not root1 and not root2:
        return True
    # root 1 和 root2 有一个非空
    elif root1 and not root2 or root2 and not root1:
        return False

    if root1.val != root2.val:
        return False

    return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)

def dfs(tree, subtree):
    if not tree:
        return False

    if tree.val == subtree.val and checkTree(tree, subtree):
        return True

    return dfs(tree.left, subtree) or dfs(tree.right, subtree)



n4 = TreeNode(110, None,None)
n5 = TreeNode(100, None,None)
n2 = TreeNode(120, n4, n5)
n3 = TreeNode(180, None,n4)
n1 = TreeNode(200, n2,n3)

print(isSubtree(n1,n2))
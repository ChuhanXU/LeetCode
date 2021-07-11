

class BST:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def insert(tree, value):
    currentNode = tree
    while True:

        if value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = BST(value)
                break
            else:
                currentNode = currentNode.right
        elif value <= currentNode.value:
            if currentNode.left is None:
                currentNode.left = BST(value)
                break
            else:
                currentNode = currentNode.left
        else:
            return tree
root = BST(10)
insert(root,5)
insert(root,11)
insert(root,12)
insert(root,1)
insert(root,2)
# 将二叉树拆成一个链表
# 如何拆左子树和右子树，返回值是什么，该如何合并
# def flatten(root):
#     helper(root)

# def helper(root):
#     if not root:
#         return None
#
#     left_last = helper(root.left)
#     right_last = helper(root.right)
#
#     if left_last:
#         left_last.right = root.right
#         root.right = root.left
#         root.left = None
#     # return 前序遍历得最后一个结点 相当于把左子树插到了根节点和右子树的中间，如果没有右子树，才返回左子树的最后一个结点，右子树也为空才返回根结点
#     print(right_last,left_last,root)
#     return right_last or left_last or root
# def flatten(root):
#     flatten_and_return_last_node(root)

    # restructure and return last node in preorder


def flatten(root):
    return dfs(root)

def dfs(root):
    if root is None:
        return None

    left_last = dfs(root.left)
    right_last = dfs(root.right)

    # connect
    if left_last is not None:
        left_last.right = root.right
        root.right = root.left
        root.left = None

    return right_last or left_last or root

print(flatten(root))

# 空间复杂度O(1)
#                      5
#                 2        3
#              1    4    6   7

# Node 1.left None return 第一次return
# def 1.right None return 第二次return left=None,right=None
# def 1.left return root 1 left = 1 第三次return
# def 1.right
# def 4.left return None
# def 2
# def 5
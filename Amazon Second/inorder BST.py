
# 怎样遍历树 和 把树转成sorted array
import collections


# def inorderTraversal(self, root):
#     if root == None:
#         return []
#
#     stack = []
#     output = []
#     node = root
#     while node or stack:
#         while node:
#             stack.append(node)
#             node = node.left
#
#         node = stack.pop()
#         output.append(node.val)
#
#         node = node.right
#     return output

def inorder(root):
    if root == None:
        return None
    stack=[]
    node = root
    result = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        result.append(node)
        node = node.right
    return result




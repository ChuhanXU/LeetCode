# 使用while loop找左右边界，使用stack遍历树找到叶子节点
def boundary(root):
    if root is None:
        return[]
    left_boundary = findleft(root.left)
    right_boundary = findright(root.right)
    leaves = findleaves(root)

    if left_boundary[-1]==leaves[0]:
        leaves = leaves[1:]
    if right_boundary[-1]==leaves[-1]:
        leaves = leaves[:-1]
    return [root.val]+left_boundary+leaves+list(reversed(right_boundary))




def findleaves(root):
    stack=[]
    stack.append(root)
    leaves=[]
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            leaves.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return leaves

def findleft(root):
    left=[]
    while root:
        left.append(root.val)
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            break
    return left

def findright(root):
    right = []
    while root:
        right.append(root.val)
        if root.right:
            root = root.right
        elif root.left:
            root = root.left
        else:
            break
    return right



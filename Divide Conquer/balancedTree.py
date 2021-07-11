
# 判断树是否平衡的条件 左子树是否平衡，右子树是否平衡
# 定义 需要返回两个值，是否平衡和树的高度
# 拆解 二叉树的拆解一般就是左子树和右子树
# 出口 if root is None: return True,0

def divideConquer(self,root):
    if not root:
        return True,0
    is_left_balanced,left_height = self.divideConquer(root.left)
    is_right_balanced,right_height = self.divideConquer(root.right)
    root_height = max(left_height,right_height)+1

    if not is_left_balanced or not is_right_balanced:
        return False,root_height
    if abs(left_height-right_height)>1:
        return False,root_height
    return True,root_height
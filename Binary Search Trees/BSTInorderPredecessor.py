# 通过二叉树的特性来找到某一节点的前驱节点
# 某一节点的中序前驱节点是该节点左子节点的右右右右子节点，如果不存在则是最近的左父亲
# 时间复杂度为O(log(n)),也可以先中序遍历，再输出这一节点的前一个位置
def inorderPredecessor(root,p):
    lowest_left_father = None
    # 先找到该节点
    if not root:
        return None
    while root != p:
        if root.val < p.val:
            lowest_left_father = root
            root = root.right
        else:
            root = root.left
    # 找它的前驱节点
    son = p.left
    ans = son
    while son:
        ans = son
        son = son.right

    return ans or lowest_left_father
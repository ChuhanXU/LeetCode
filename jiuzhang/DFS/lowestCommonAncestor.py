
# Input：{4,3,7,#,#,5,6},3,5
# Output：4
# Explanation：
#  For the following binary tree:
#
#       4
#      / \
#     3   7
#        / \
#       5   6
#
#  LCA(3, 5) = 4
# 不确定两个节点是否都在树中
def lowestCommonAncestor(root,A,B):
    return dfs(root,A,B)

# 如果A和 B都在，return LCA
# 如果只有A在，return A
# 如果只有B在，return B
# 如果 A,B都不在，return None

def dfs(root,A,B):
    if root is None:
        return None
    if root == A or root == B:
        return root
    left_result = dfs(root.left,A,B)
    right_result = dfs(root.right,A,B)

#     A 和 B 一边一个
    if left_result and right_result:
        return root
#     左子树有一个点或者左子树有LCA
    if left_result:
        return left_result
#     右子树有一个点或者右子树有LCA
    if right_result:
        return right_result
#     左右子树都没有
    return None


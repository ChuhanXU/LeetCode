
# 输入:
# {6,2,8,0,4,7,9,#,#,3,5}
# 2
# 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 从根节点root开始，遍历整棵树
# 如果root等于p或q，那么root即为p和q的LCA。
# 如果root同时大于p和q，说明p和q 都在左子树上，那么将root.left作为根节点，继续第一步的操作。
# 如果root同时小于p和q，说明p和q 都在右子树上，那么将root.right作为根节点，继续第一步的操作。
# 如果以上情况都不成立，说明p和q分别在两颗子树上，那么root就是p和q的LCA。
def lcaOfBinarySearchTree(root,A,B):
    return dfs(root,A,B)
def dfs(root,A,B):
    if root is None:
        return None
    if root == A or root == B:
        return root
    if A.val<root.val and B.val<root.val:
        return dfs(root.left,A,B)
    if A.val>root.val and B.val>root.val:
        return dfs(root.right,A,B)
    return root

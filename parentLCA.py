
# 给一棵二叉树和二叉树中的两个节点，找到这两个节点的最近公共祖先LCA。
#
# 两个节点的最近公共祖先，是指两个节点的所有父亲节点中（包括这两个节点），离这两个节点最近的公共的节点。
#
# 每个节点除了左右儿子指针以外，还包含一个父亲指针parent，指向自己的父亲。
# 输入：{4,3,7,#,#,5,6},3,5
# 输出：4
# 解释：
#      4
#      / \
#     3   7
#        / \
#       5   6
# LCA(3, 5) = 4
# 建立集合parentSet，用于存储A的祖先节点。
# 首先，从A向上遍历到root，将路径中的节点都存储到parentSet中。
# 然后，从B向上遍历，判断经过的每个节点是否同时也在parentSet中，第一个出现在parentSet中的点即为A和B的最近公共祖先

def lca(root,A,B):
    parentSet = set()
    cur = A
    while cur is not root:
        parentSet.add(cur)
        cur = cur.parent

    while B is not root:
        if B in parentSet:
            return B
        B = B.parent

    return root

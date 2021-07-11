
# 输入:
# {1,-5,2,1,2,-4,-5}
# 输出:1
# 说明
# 这棵树如下所示：
#      1
#    /   \
#  -5     2
#  / \   /  \
# 1   2 -4  -5
# 整颗树的和是最小的，所以返回根节点1.

# 使用全局变量
# class Solution:
#
#     def findSubtree(self,root):
#         self.minimum_subtree_root = None
#         self.minimum_weight = float('inf')
#         self.getTreeSum(root)
#
#
#         return self.minimum_subtree_root
#     def getTreeSum(self,root):
#         if root is None:
#             return 0
#         left_weight = self.getTreeSum(root.left)
#         right_weight = self.getTreeSum(root.right)
#         root_weight= left_weight+right_weight+root.val
#
#         if root_weight<self.minimum_subtree_root:
#             self.minimum_subtree_root = root
#             self.minimum_weight = root_weight
#
#         return root_weight
# 不使用全局变量的分治法,把想要的变量做为return的值
# 子树的最小值有三个可能，左子树的最小值，右子树的最小值，这两个左右子树的根结点的最小值
# 左子树的最小值不一定是这个左子树以根结点开始的最小值
import sys


class Solution:
    def findSubtree(self,root):
        minimum,subtree,sum_of_root=self.dfs(root)
        return subtree
    def dfs(self,root):
        if root is None:
            return sys.maxsize,None,0
        left_minimum,left_subtree,left_sum=self.dfs(root.left)
        right_minimum,right_subtree,right_sum = self.dfs(root.right)

        sum_of_root = left_sum+right_sum+root.val
        if left_minimum==min(left_minimum,right_minimum,sum_of_root):
            return left_minimum,left_subtree,sum_of_root
        if right_minimum==min(left_minimum,right_minimum,sum_of_root):
            return right_minimum,right_subtree,sum_of_root
        # 如果左右节点都不是最小，就是根节点
        return sum_of_root,root,sum_of_root





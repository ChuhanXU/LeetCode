
# dfs 要知道的三个东西
# 1.传入什么参数
# 2.返回什么参数
# 3.如何拆解，左右两边
# 不能只求子树的最大路径，还需要求最大的链
# 这棵树的最大路径应该为左边的最大路径，右边的最大路径，和左子树加上右子树的最大链
import sys


def maxPathSum(self,root):
    ans,chain= self.dfs(root)
    return ans
def dfs(self,root):
    if not root:
        # 如果只有一个单节点-1，就会返回0，不符合题目要求，所以要使用return(-sys.maxsize,0)
        # return(0,0)
        return (-sys.maxsize, 0)

    left_max_path, left_max_chain = self.dfs(root.left)
    right_max_path, right_max_chain = self.dfs(root.right)

    max_path = max(left_max_path,right_max_path,left_max_chain+right_max_chain+root.val)
    # 如果算出的结果是个负数，直接舍弃这个链，将结果记为0
    # max_chain = max(left_max_chain,right_max_chain) + root.val 不行
    # 如果左右两边都是负数，it should choose nothing, but with this formula, it will choose
    # a bigger one between two minus number.
    # max_chain = max(left_max_chain,right_max_chain, 0)+root.val 不行，见下
    max_chain = max(max(left_max_chain,right_max_chain)+root.val,0)
    # the minimum of max_chain number should be 0

    return(max_path,max_chain)
#    1         -2节点的max_path和max_chain 为 -2 -2， 3节点的max_path和max_chain为3 3
#  /  \
# -2  3        -2 3 （-2 +3）+1 = 2 所以返回了3，但是答案应该是4，因为左链可以为0

# 输入：
# {1,-5,11,1,2,4,-2}
# 输出：11
# 说明:
# 这棵树如下所示：
#      1
#    /   \
#  -5     11
#  / \   /  \
# 1   2 4    -2
# 11子树的平均值是4.333，为最大的。
import sys

def findAverage(root):

    if root in None:
        return
    max_avg,max_tree,size,sum=dfs(root)
    return max_tree

def dfs(root):
    if root is None:
        return -sys.maxsize,None,0,0
    l_avg,l_maxtree,l_num,l_sum=dfs(root.left)
    r_avg,r_maxtree,r_num,r_sum=dfs(root.right)

    sum,num = l_sum+r_sum+root.val,l_num+r_num+1
    average = sum/num


    if l_avg == max(l_avg,r_avg,average):
        return l_avg,l_maxtree,num,sum
    if r_avg == max(l_avg, r_avg, average):
        return r_avg, r_maxtree, num, sum

    return average,root,num,sum


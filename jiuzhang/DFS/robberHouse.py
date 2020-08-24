# 在上次打劫完一条街道之后和一圈房屋之后，窃贼又发现了一个新的可以打劫的地方，
# 但这次所有的房子组成的区域比较奇怪，聪明的窃贼考察地形之后，发现这次的地形是一颗二叉树。
# 与前两次偷窃相似的是每个房子都存放着特定金额的钱。你面临的唯一约束条件是：
# 相邻的房子装着相互联系的防盗系统，且当相邻的两个房子同一天被打劫时，该系统会自动报警。
# 输入:  {3,2,3,#,3,#,1}
# 输出: 7
# 解释:
# 最多能偷 3 + 3 + 1 = 7.
#   3
#  / \
# 2   3
#  \   \
#   3   1
# 同diameter of tree那道题类似，需要进行拆解成两个返回值，要根结点的最大值和不要根结点的最大值
def houseRobber3(self,root):
    not_in_ans,in_ans = self.dfs(root)
    return max(in_ans,not_in_ans)

def dfs(self,root):
    if not root:
        return(0,0)

    left_not_in_ans,left_in_ans = self.dfs(root.left)
    right_not_in_ans,right_in_ans = self.dfs(root.right)

    in_ans = left_not_in_ans + right_not_in_ans + root.val
    # but, there is another situation that if we don't choose the root node, we are not necessarily to choose both left and right of that root node
    # what we need to do is to compare the profit that we choose this node and the profit that we don't choose that node to find the bogger one as our profit for this node
    not_in_ans = max(left_in_ans,left_not_in_ans)+max(right_in_ans,right_not_in_ans)

    return(not_in_ans,in_ans)


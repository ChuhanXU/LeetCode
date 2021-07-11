
# Input：root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# Output：3
# Explanation：
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# find the number of paths that sum to a given value
#
def pathsum(root,sum):
    if root is None:
        return 0
    result = dfs(root,sum,0)+pathsum(root.left,sum)+pathsum(root.right,sum)
    return result
def dfs(root,sum,tmp):
    if root is None:
        return 0
    flag =0
    if sum==tmp+root.val:
        flag=1
    return flag+dfs(root.left,sum,tmp+root.val)+dfs(root.right,sum,tmp+root.val)

# Input:tree = [5,4,8,11,#,13,4,7,2,#,#,#,#,#,1], sum = 22
# Output: true
# Explanation: Given the below binary tree
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

def pathSum(self, root, sum):
    # Write your code here.
    if root == None:
        return False;
    elif (root.val == sum and root.left == None and root.right == None):
        return True;
    else:
        return self.pathSum(root.left, sum - root.val) or self.pathSum(root.right, sum - root.val);


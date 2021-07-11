# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
#O(nh)
def find_two_sum_bst(root,target):
    if not root:
        return False
    begin = root
    end = root
    while begin.left:
        begin=begin.left
    while end.right:
        end = end.right
    while begin and end and begin is not end:
        if begin.val+end.val<target:
            begin=begin.getnext(root,begin)
        elif begin.val+end.val>target:
            end=end.getpre(root,end)
        else:
            return True
    return False

def getnext(root,current):
    if current is None or root is None:
        return None
    if current.val>root.val:
        return getnext(root.right,current)
    else:
        left = getnext(root.left,current)
        if left:
            return left
        else:
            return root

# #   4
# # /  \
#  2    5
#  /
# 1

1

# def getpre(root,current):
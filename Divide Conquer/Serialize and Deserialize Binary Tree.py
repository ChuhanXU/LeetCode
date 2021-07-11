class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None
# 输入：{3,9,20,#,#,15,7}
# 输出：{3,9,20,#,#,15,7}
# 解释：
# 二叉树 {3,9,20,#,#,15,7}，表示如下的树结构：
# 	  3
# 	 / \
# 	9  20
# 	  /  \
# 	 15   7
# 它将被序列化为 {3,9,20,#,#,15,7}
import collections


def serialize(root):
    if not root:
        return{}
    queue = collections.deque()
    queue.append([root])
    bfs_order = []
    while queue:
        node = queue.popleft()
        bfs_order.append(str(node.val) if node else '#')

        if node:
            queue.append(node.left)
            queue.append(node.right)
    return ' '.join(bfs_order)

def deserialize(data):
    if not data:
        return None
    # 先把字符串转为TreeNode
    bfs_order =[TreeNode(int(val)) if val !='#'else None for val in data.split()]
    root = bfs_order[0]
    fast_index = 1
    nodes,slow_index = [root],0
    while slow_index<len(nodes):
        node = nodes[slow_index]
        slow_index+=1
        node.left = bfs_order[fast_index]
        node.right = bfs_order[fast_index+2]
        fast_index+=2
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
    return root
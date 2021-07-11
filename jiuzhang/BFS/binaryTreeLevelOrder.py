
# bfs
import collections
def aa(tree):
    if not tree:
        return None
    queue = collections.deque([tree])
    result = []
    while queue:
        result.append([node.val for node in queue])
        for i in range (len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result






















def binaryTreeLevelOrder(root):
    if not root:
        return []
    queue=collections.deque([root])
    result=[]
    while queue:
        result.append([node.val for node in queue])
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
#      1
#  2     3
#4   5
# queue  4 5
# result 1 2 3 4 5
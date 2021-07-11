
# 设计实现一个带有下列属性的二叉查找树的迭代器：
# next()返回BST中下一个最小的元素
#
# 元素按照递增的顺序被访问（比如中序遍历）
# next()和hasNext()的询问操作要求均摊时间复杂度是O(1)
# 输入：{10, 1, 11,  # ,6,#,12}
#     输出：[1, 6, 10, 11, 12]
# 解释：
# 二叉查找树如下:
# 10
# / \
# 1
# 11
# \ \
# 6  12
# 可以返回二叉查找树的中序遍历[1, 6, 10, 11, 12]
# 利用stack中序遍历的模板
# stack中保存一路走到当前节点的所有节点，stack.peek()指向iterator指向的当前节点
def _init_(self,root):
    self.stack=[]
    while root!=None:
        self.stack.append(root)
        root = root.left

def hasNext(self):
    return len(self.stack)>0

def next(self):
    node = self.stack.pop()
    next_node=node
    if node.right:
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
    return next_node
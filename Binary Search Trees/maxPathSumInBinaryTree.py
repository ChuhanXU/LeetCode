# class的一个构造器
class BST:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def getMin(self):
        currentNode = self
        while currentNode is not None:
            currentNode = currentNode.left
        return currentNode.value


def insert(tree,value):
    currentNode = tree
    while True:

        if value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = BST(value)
                break
            else:
                currentNode = currentNode.right
        elif value <= currentNode.value:
            if currentNode.left is None:
                currentNode.left = BST(value)
                break
            else:
                currentNode = currentNode.left
        else:
            return tree


def maxPathSum(tree):
    arrayLeft = calculateBranchSums(tree.left, 0, [])
    arrayRight = calculateBranchSums(tree.right, 0, [])
    arraySortedLeft = sorted(arrayLeft)
    arraySortedRight = sorted(arrayRight)
    return arraySortedLeft[len(arraySortedLeft) - 1] + arraySortedRight[len(arraySortedRight) - 1] + tree.value


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return sums
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
    return sums

def iterativeInOrderTraversal(tree,callback):
    previousNode = None
    currentNode = tree
    while currentNode is not None:
        if previousNode is None or previousNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        # 从左边上去说明中间结点还没有callback 右结点也没有访问
        elif previousNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        # 从右边上去说明中间结点和右边结点都已经callback，要去当前结点的父结点了
        else:
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode
# 求二叉树的最大深度
def maxDepth(tree):
    if tree is None:
        return 0
    left = maxDepth(tree.left)
    right = maxDepth(tree.right)
    return max(right,left)+1

root = BST(10)
insert(root,5)
insert(root,15)
insert(root,12)
insert(root,16)
# insert(root,2)
# insert(root,5)
# insert(root,13)
# insert(root,22)
# insert(root,1)
# insert(root,14)
# remove(root,14)
# remove(root,1)
# print(inOrderTraverses(root,[]))
# print(contain(root,11))
# print(nodeDepthsIterative(root))
# print(inOrderTraverses(root,[]))
# print(invertBinaryTree(root))
# print(branchSums(root))
print(maxPathSum(root))
# print(maxDepth(root))




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





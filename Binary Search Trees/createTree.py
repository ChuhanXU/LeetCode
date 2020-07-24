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

def contain(tree,value):
    currentNode = tree
    while currentNode is not None:
        if value > currentNode.value:
            currentNode = currentNode.right
        elif value < currentNode.value:
            currentNode = currentNode.left
        else:
            return True
    return False




def inOrderTraverses(tree,array):
    if tree is not None:
        inOrderTraverses(tree.left,array)
        array.append(tree.value)
        inOrderTraverses(tree.right, array)
    return array


def remove(tree, value, parentNode=None):
    currentNode = tree
    while currentNode is not None:
        if value > currentNode.value:
            parentNode = currentNode
            currentNode=currentNode.right
        elif value < currentNode.value:
            parentNode = currentNode
            currentNode = currentNode.left
        else:

            if currentNode.left is not None and currentNode.right is not None:
                currentNode.value = currentNode.right.getMin()
                currentNode.right.remove(currentNode.value, parentNode)
            elif parentNode is None:
                if currentNode.left is not None:
                    currentNode.value = currentNode.left.value
                    currentNode.right = currentNode.left.right
                    currentNode.left = currentNode.left.left
                elif currentNode.right is not None:
                    currentNode.value = currentNode.right.value
                    currentNode.left = currentNode.right.left
                    currentNode.right = currentNode.right.right
                else:
            # there is only one node and it is root node
                    currentNode = None
            elif parentNode.left == currentNode:
                parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
            elif parentNode.right == currentNode:
                 parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
            break
    return tree

def nodeDepthsRecursive(tree,depth=0):
    if tree is None:
        return 0
    return depth + nodeDepthsRecursive(tree.left,depth+1)+nodeDepthsRecursive(tree.right,depth+1)
# 通过一个栈，将树中的结点放入，并依次弹出，如果弹出的结点为空就skip
# O(N) O(h)
def nodeDepthsIterative(tree):
    sumOfDepths = 0
    stack = [{"node":tree,"depth":0}]
    while len(stack)>0:
        nodeInfo = stack.pop()
        node , depth = nodeInfo["node"],nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node":node.left,"depth":depth + 1})
        stack.append({"node":node.right,"depth":depth+1})
    return sumOfDepths

def invertBinaryTree(tree):
    queue = [tree]
    while len(queue)>0:
        current = queue.pop(0)
        if current is None:
            continue
        swap(current)
        queue.append(current.left)
        queue.append(current.right)
    return inOrderTraverses(tree,[])

def swap(tree):
    tree.left,tree.right = tree.right,tree.left


def branchSums(tree):
    return calculateBranchSums(tree, 0, [])

def maxPathSum(tree):
    array = calculateBranchSums(tree, 0, [])
    arraySorted = sorted(array)
    return arraySorted[0] + arraySorted[2] - tree.value

# 递归的时候一般都是退出的条件，不会让你找一个条件去递归
def calculateBranchSums(tree, runningSum, sums):
    if tree is None:
        return

    newRunningSum = runningSum + tree.value
    if tree.left is None and tree.right is None:
        sums.append(newRunningSum)
        return
    calculateBranchSums(tree.left, newRunningSum, sums)
    calculateBranchSums(tree.right, newRunningSum, sums)
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





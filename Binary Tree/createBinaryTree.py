class BST:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def insert(tree, value):
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



root = BST(10)
insert(root,5)
insert(root,15)
insert(root,7)


#  10
# /  \
# 5  15
#  \
#  7

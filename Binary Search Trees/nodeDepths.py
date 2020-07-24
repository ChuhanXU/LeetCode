def nodeDepthsRecursive(tree,depth=0):
    if tree is None:
        return 0
    return depth + nodeDepthsRecursive(tree.left,depth+1)+nodeDepthsRecursive(tree.right,depth+1)

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
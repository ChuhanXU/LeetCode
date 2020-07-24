def branchSums(tree):
    return helper(tree.left,0,[])

def helper(tree,runningSum,sums):
    if tree is None:
        return

    newRunningSum = runningSum + tree.value
    if tree.left is None and tree.right is None:
        sums.append (newRunningSum)
        return
    helper(tree.left,newRunningSum,sums)
    helper(tree.right,newRunningSum,sums)
    return sums


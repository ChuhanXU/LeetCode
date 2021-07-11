
# 分治法vs遍历法
# 分治法 整棵树的路径=左子树路径+右子树路径
# 遍历法
def binaryTreePaths(self,root):
    if not root:
        return
    path = []
    paths = []
    path.append(str(root.val))
    self.dfs(root,path,paths)
    return paths

def dfs(self,root,path,paths):
    if root.left is None and root.right is None:
        print(path)

        paths.append('->'.join(path))
        return paths

    if root.left:
        path.append(str(root.left.val))
        self.dfs(root.left, path, paths)
        path.pop()

    if root.right:
        path.append(str(root.right.val))
        self.dfs(root.right, path, paths)
        path.pop()
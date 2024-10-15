class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leafPath(root, sum, targetSum):
    if not root:
        return False
    sum+=root.val

    if not root.left and not root.right and sum == targetSum:
        return True
    if leafPath(root.left, sum, targetSum):
        return True
    if leafPath(root.right, sum, targetSum):
        return True
    return False

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return leafPath(root,0,targetSum)
        
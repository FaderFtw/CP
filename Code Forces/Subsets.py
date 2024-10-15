class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val >= root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def getSubsets(root,subsets, path):
    if not root:
        return []
    subsets.append([root.val])
    path.append(root.val)
    

    if not root.left and not root.right:
        return [path]
    if root.left:
        subsets.append(getSubsets(root.left,subsets, path))
    if root.right:
        subsets.append(getSubsets(root.right,subsets, path))

    path.pop()
    return [path]


root = None
values = [5, 3, 7, 2]

for val in values:
    root = insert(root, val)

subsets=[]
getSubsets(root,subsets,[])
print(subsets)
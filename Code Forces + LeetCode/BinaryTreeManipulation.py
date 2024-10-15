from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val >= root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    level = 1
    while curr and curr.left:
        curr = curr.left
        level +=1
    return (curr,level)

# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root

from collections import deque

def print_tree_visual(root,levels):
    queue = deque()

    if root:
        queue.append(root)
    
    spacing = ' '*(levels)
    while len(queue) > 0:
        if spacing != ' ':
            s=spacing
        else:
            s=''
        for i in range(len(queue)):
            curr = queue.popleft()
            s=s+str(curr.val)+' '
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        spacing = spacing[:len(spacing)-1]
        print(s[:len(s)-1])

def inorder(root):
    if not root:
        return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)

root = None
values = [5, 3, 7, 2, 4, 6, 8]

for val in values:
    root = insert(root, val)

(minNode,levels) = minValueNode(root)
print_tree_visual(root,levels)
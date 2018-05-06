class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def averageOfLevels(root):
    root = TreeNode(x)
    if root.left and root.right == 0:
        return root.val
    else:
        
    
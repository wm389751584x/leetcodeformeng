# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        res = [0]
        if not root: return 0
        self.treeSum(root, res, root.val)
        
        return res[0]
        
    
    def treeSum(self, root, res, path):
        if not root.left and not root.right:
            res[0] += path
        if root.left:
            self.treeSum(root.left, res, path*10 + root.left.val)
        if root.right:
            self.treeSum(root.right, res, path*10 + root.right.val)
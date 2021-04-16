# Definition for a binary tree node.
# pass by reference
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def inorder(node, res):
            if node:
                inorder(node.left, res)
                if low <= node.val <= high:
                    res.append(node.val)
                inorder(node.right, res)
        res = []
        inorder(root, res)
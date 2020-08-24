# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.helper(root)
        return max(res)
    
    def helper(self, root):
        if not root: return [0, 0]
        res = [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res[0] = max(left[0] + left[1]) + max(right[0] + right[1])
        res[1] = left[0] + right[0] + root.val
        return res
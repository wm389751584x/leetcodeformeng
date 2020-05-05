# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root)

    def helper(self, node):
        if not node: return 0
        return min(self.helper(node.left), self.helper(node.right)) + 1

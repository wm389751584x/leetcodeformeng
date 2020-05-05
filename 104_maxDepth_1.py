# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        depth = 0
        return self.seach(root, depth)
    
    def seach(self, node, depth):
        if not node: return depth
        depth += 1
        return max(self.seach(node.left, depth), self.seach(node.right, depth))


if __name__ == "__main__":
    pass

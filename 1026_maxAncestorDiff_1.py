# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max = 0
        self.dfs(root)
        return self.max

    def dfs(self, root, nmax=0, nmin=5001):
        if not root: return 0
        nmin = min(nmin, root.val)
        nmax = max(nmax, root.val)
        self.max = max(self.max, abs(nmax - nmin))
        self.dfs(root.left, nmax, nmin)
        self.dfs(root.right, nmax, nmin)

if __name__ == "__main__":
    pass
    
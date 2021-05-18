# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root: return 0
        return self.dfs(root, float("-inf"))
        
        
    def dfs(self, node, maxval):
        
        # base case
        if not node: return 0
        temp = 0
        left = self.dfs(node.left, max(maxval, node.val))
        right = self.dfs(node.right, max(maxval, node.val))
        
        return left + right + (1 if node.val > maxval else 0)



if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(s.goodNodes(root))
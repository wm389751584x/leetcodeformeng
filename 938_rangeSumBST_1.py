# Definition for a binary tree node.
# pass by value
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def inorder(node):
            if node:
                inorder(node.left)
                if low <= node.val <= high:
                    self.res += node.val
                inorder(node.right)
        self.res = 0
        inorder(root)
        return self.res 


if __name__ == "__main__":
    root = TreeNode(0)
    Solution().rangeSumBST(root, 0, 0)
            
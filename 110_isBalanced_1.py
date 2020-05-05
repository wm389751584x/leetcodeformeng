# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: 
            return True
        elif abs(self.helper(root.left) - self.helper(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        

    def helper(self, node):
        if node == None: return 0
        return max(self.helper(node.left), self.helper(node.right)) + 1



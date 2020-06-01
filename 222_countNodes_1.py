# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
            if not root: return 0
            self.num = 0

            self.tree(root)
            return self.num
        
    def tree(self, node):
        if not node:
            return
        self.num += 1
        self.tree(node.left)
        self.tree(node.right)



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

print(Solution().countNodes(node1))
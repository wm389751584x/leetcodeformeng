# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.helper(root.left, root.right)
    
    def helper(self, node1, node2):
        if not node1 and not node2: 
            return True
        elif node1.val == node2.val:
            return self.helper(node1.left, node2.right) and \
                self.helper(node1.right, node2.left)
        else:
            return False
            

if __name__ == "__main__":
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    assert s.isSymmetric(node1) == False
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        return self.helper(root, sum)

    def helper(self, node, sum):
        # last leaf
        if node.left == None and node.right == None:
            if sum - node.val == 0:
                return True
            else:
                return False
        a = b = False
        if node.left:
            a = self.helper(node.left, sum - node.val)
        if node.right:
            b = self.helper(node.right, sum - node.val)
        return a or b


if __name__ == "__main__":
    node1 = TreeNode(7)
    node2 = TreeNode(0)
    node3 = TreeNode(-1)
    node4 = TreeNode(-6)
    node5 = TreeNode(1)
    node6 = TreeNode(-7)
    node1.left = node2
    node2.left = node3
    node2.right = node4
    node3.right = node5
    node5.left = node6
    
    assert Solution().hasPathSum(node1, 0) == True
            
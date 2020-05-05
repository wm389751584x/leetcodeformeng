from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, node, res):
        if node.left == None and node.right == None:
            res.append(node.val)
        elif node.left == None:
            res.append(node.val)
            self.inorder(node.right, res)
        elif node.right == None:
            self.inorder(node.left, res)
            res.append(node.val)
        else:
            self.inorder(node.left, res)
            res.append(node.val)
            self.inorder(node.right, res)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    assert Solution().inorderTraversal(n1) == [1, 3, 2]
from typing import List
# Iterative Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # need to use stack
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            # 注意入栈的顺序.
            stack.append(node.right)
            stack.append(node.right)
        return res

        
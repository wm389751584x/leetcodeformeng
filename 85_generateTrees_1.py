from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: 
            return []
        else:
            return self.helper(1, n)

    def helper(self, left, right):
        if left > right:
            return [None]
        for i in range(left, right + 1):
            left_nodes = self.helper(left, i - 1)
            right_nodes = self.helper(i + 1, right)
        for lnode in left_nodes:
            for rnode in right_nodes:
                


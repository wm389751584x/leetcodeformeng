# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        place = []
        self.dfs(root, place)
        for i in range(len(place) - 1):
            place[i].left = None
            place[i].right = place[i+1]

    def dfs(self, node, place):
        if not node:
            return
        place.append(node)
        self.dfs(node.left, place)
        self.dfs(node.right, place)
        
        
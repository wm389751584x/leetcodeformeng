from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        res = []
        self.search()
        return res

    def search(self, node, temp, sum, res):
        if not node.left and not node.right:
            if sum - node.val == 0:
                temp.append(node.val)
                res.append(temp[:])
                temp.pop()
            return
        if node.left:
            self.search(node.left, temp + [node.val], sum - node.val, res)
        if node.right:
            self.search(node.right, temp + [node.val], sum - node.val, res)

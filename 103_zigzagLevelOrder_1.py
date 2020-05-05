# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        nodes = [root]
        self.helper(nodes, res)
        for i in range(1, len(res), 2):
            res[i].reverse()
        return res

    def helper(self, nodes, res):
        if not nodes:
            return
        vals = []
        temp = []
        for node in nodes:
            vals.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        res.append(vals)
        nodes = temp
        self.helper(nodes, res)
# Definition for a binary tree node.
# Breadth first search
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        nodes = [root]
        self.helper(nodes, res)
        return res

    def helper(self, nodes, res):
        if not nodes:
            return
        temp = []
        vals = []
        for node in nodes:
            vals.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        res.append(vals)
        nodes = temp
        self.helper(nodes, res)


if __name__ == "__main__":
    pass
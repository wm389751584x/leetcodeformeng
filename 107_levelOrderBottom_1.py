from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        nodes = [root]
        self.travel(nodes, res)
        return reversed(res)
    
    def travel(self, nodes, res):
        if not nodes: return 
        temp = []
        values = []
        for node in nodes:
            values.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        res.append(values[:])
        nodes = temp
        self.travel(nodes, res)


if __name__ == "__main__":
    pass

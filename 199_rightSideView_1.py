# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return None
        res = []
        level = [root]
        self.helper(level, res)
        return res
    
    def helper(self, level, res):
        if not level:
            return
        else:
            res.append(level[-1].val)
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.apend(node.right)
            self.helper(temp, res)


if __name__ == "__main__":
    pass
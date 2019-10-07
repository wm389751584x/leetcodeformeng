# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, min, max):
        if min > max: return [None]
        
        res = []
        
        for curr in range(min, max + 1):
            left = self.helper(min, curr - 1)
            right = self.helper(curr + 1, max)
            
            for l in left:
                for r in right:
                    root = TreeNode(curr)
                    root.left = l
                    root.right = r
                    res.append(root)
                    
        return res
        
    def generateTrees(self, n):
        
        if n == 0:
            return []
        else:
            return self.helper(1, n)


print(Solution().generateTrees(3))
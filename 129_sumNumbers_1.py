# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        res = [0]
        
        if not root: return 0
        
        self.treeSum(root, res, '')
        
        return res[0]
        
    
    def treeSum(self, root, res, temp):
        if not root: return
        
        if not root.left and not root.right:
            temp += str(root.val)
            res[0] += int(temp)
            temp = temp[:-1]
            return

        self.treeSum(root.left, res, temp + str(root.val))
        self.treeSum(root.right, res, temp + str(root.val))


if __name__ == "__main__":
    pass
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = self.inOrder(root)

        l, r = None, None
        for i in range(len(res)-1):
            if res[i].val > res[i+1].val:
                l = res[i]
                break
        
        for i in range(1, len(res)):
            if res[i].val < res[i-1].val:
                r = res[i]
        
        l.val, r.val = r.val, l.val
            
        
    
    def inOrder(self, root):
        res = []
        if root:
            res = self.inOrder(root.left)
            res.append(root)
            res += self.inOrder(root.right)
        return res




if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)

    Solution().recoverTree(root)
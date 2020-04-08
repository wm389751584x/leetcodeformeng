# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if not root: return []
        
        res, path = [], []
        self.dfs(root, path, res)
        return res
    
        
    def dfs(self, root, path, res):
        
        if not root: return 

        path.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(path))
        self.dfs(root.left, path, res)
        self.dfs(root.right, path, res)
        path.pop()


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    print(Solution().binaryTreePaths(root))
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root):
        self.res = 0
        def dfs(curr):
            # base case: when current node is none
            if not curr: return 2

            # post-order traversal
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            # case 1: left right both covered
            if left == 2 and right == 2:
                return 0
            
            # case 2: either left or right is no cover
            if left == 0 or right == 0:
                self.res += 1
                return 1
            
            # case 3: either left or right has camera
            if left == 1 or right == 1:
                return 2

        # case 4: check root node coverage
        if dfs(root) == 0:
            self.res += 1
        return self.res



if __name__ == "__main__":
    node0 = TreeNode(0)
    Solution().minCameraCover(node0)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.sum = 0
        self.postOrder(root)
        return self.sum

    def postOrder(self, root):
        if not root: return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        self.sum += abs(left - right)
        return left + right + root.val


if __name__ == "__main__":
    # assert Solution().findTilt([1,2,3]) == 1
    pass
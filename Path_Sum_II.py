class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution:
    def pathSum(self, root: TreeNode, sum: int):

        ans, test = [], []

        def find_path(ans, test, sum, root):

            if root == None:
                return
            if root.left == None and root.right == None:
                test.append(root.val)
                total = 0
                for val in test:
                    total += val
                if total == sum:
                    ans.apend(test[:])
                test.pop()

            else:
                test.append(root.val)
                find_path(ans, test, sum, root.left)
                find_path(ans, test, sum, root.right)
        print(ans)


node = TreeNode(5)
node.left = TreeNode(7)
node.right = TreeNode(9)

mysol = Solution()

mysol.pathSum(node, 14)
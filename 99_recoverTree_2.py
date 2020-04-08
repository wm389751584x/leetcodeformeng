class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
class Solution(object):
    def __init__(self):
        self.node1 = None
        self.node2 = None
        self.pre = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.__scan(root)

    def __scan(self, root):
        if root is None: return

        self.__scan(root.left)
        if self.pre:
            if root.val < self.pre.val:
                if not self.node1:
                    self.node1 = self.pre
                    self.node2 = root
                else:
                    self.node2 = root

        self.pre = root
        self.__scan(root.right)


if __name__ == "__main__":
    None
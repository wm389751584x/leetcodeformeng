class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return False
        otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visted in
        a pre-order traversal."""
        return self.preorder_print(self.root, "")

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution"""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or (
                    self.preorder_search(start.right, find_val))
        else:
            return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        else:
            return traversal

    def is_same_tree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.same_tree_helper(p.root, q.root)

    def same_tree_helper(self, p, q):

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.value != q.value:
            return False
        else:
            return self.same_tree_helper(p.left, q.left) and self.same_tree_helper(p.right, q.right)

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.cycleHelper(head.root)

    def cycleHelper(self, node):
        while True:
            if node.next is None:
                return False
            else:
                p = node.next
            if p.next is None:
                return False
            else:
                q = p.next
            if q.next is None:
                return False
            else:
                w = q.next
            if p == q:
                return True


# Set up tree
tree1 = BinaryTree(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)

tree2 = BinaryTree(10)
tree2.root.left = Node(5)
tree2.root.left.right = Node(15)

print(BinaryTree().isSymmetric(tree1))

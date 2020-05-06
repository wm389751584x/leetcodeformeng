"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # breath first search
        dummy = root
        if not root: return None
        level = [root]

        while level:
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            for i in range(len(temp) - 1):
                temp[i].next = temp[i+1]
            level = temp
        return dummy


if __name__ == "__main__":
    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.left = node2
    node1.right = node3
    assert s.connect(node1)

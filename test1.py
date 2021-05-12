# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.makeTree(head)
    
    # since the linked-list is already sorted, 
    # so we need find the middle point which is slow, fast pointer
    def makeTree(self, slist):
        if not slist: return None
        pre = slow = fast = slist
        if slist.next == None:
            node = TreeNode(val = slist.val)
            node.left = None
            node.right = None
            return node
        head_left = slist
        
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        head_right = slow.next
        pre.next = None
        
        node = TreeNode(val=slow.val)
        node.left = self.makeTree(head_left)
        node.right = self.makeTree(head_right)
        return node


if __name__ == "__main__":
    s = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(2) 
    list1.next.next = ListNode(3)
    s.sortedListToBST(list1)
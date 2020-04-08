# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        pre, slow, fast =head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l1 = head
        l2 = self.reverse(slow)
        return self.reorder(l1, l2)
        
    def reverse(self, l2):
        if not l2 or not l2.next: return l2
        pre = None
        curr = l2
        pos = l2.next
        
        while pos:
            curr.next = pre
            pre = curr
            curr = pos
            pos = pos.next
        curr.next = pre
        return curr
    
    def reorder(self, l1, l2):
        node = ListNode(0)
        curr = node
        
        if not l1: return l2
        if not l2: return l1
        while l1 and l2:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
            curr.next = l2
            l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return node.next


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    s = Solution()
    s.reorderList(node)
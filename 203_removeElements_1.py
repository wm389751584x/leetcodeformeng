# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        node = head
        while node:
            if node.val == val:
                pre.next = node.next
                node = node.next
            else:
                pre = pre.next
                node = node.next
        return dummy.next
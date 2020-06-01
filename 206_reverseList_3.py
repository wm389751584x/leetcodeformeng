# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        new_head = None

        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head


if __name__ == "__main__":
    pass
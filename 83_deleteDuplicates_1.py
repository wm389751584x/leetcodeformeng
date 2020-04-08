# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        slow = fast = head
        while head.next:
            fast = fast.next
            if slow.val != fast.val:
                slow.next = fast
                slow = fast

        slow.next = fast.next

        return head


if __name__ == "__main__":
    pass
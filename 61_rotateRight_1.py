# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        pre, curr = head, head
        count = 0
        while curr:
            pre = curr
            curr = curr.next
            count += 1
        pre.next = head

        k %= count

        while k > 0:
            pre = pre.next
            k -= 1

        temp = pre.next
        pre.next = None
        
        return temp
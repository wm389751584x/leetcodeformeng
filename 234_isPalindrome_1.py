# Definition for singly-linked list.
# Palindrome Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow.next == fast:
            return slow.val == fast.val
        
        slow = slow.next
        new_head = None
        
        while slow:
            p = slow
            slow = slow.next
            p.next = new_head
            new_head = p
            
        while new_head:
            if head.val != new_head.val:
                return False
            else:
                head = head.next
                new_head = new_head.next
        return True
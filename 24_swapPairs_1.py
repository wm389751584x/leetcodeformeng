# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        pre = dummy = ListNode(-1)
        left = head
        dummy.next = head
        right = head.next
        
        
        while right and right.next:
            left.next = right.next
            right.next = pre.next
            pre.next = right
            left, right = right, left
            right = right.next
            if right:
                right = right.next
            else:
                break
            left = left.next.next
            pre = pre.next.next
            
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    Solution().swapPairs(l1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        p = dummy = ListNode(0)

        while l1 & l2:
            
            if l1.val < l2.val:
                p.next = l1
                p = l1
                l1 = l1.next
            else:
                p.next = l2
                p = l2
                l2 = l2.next
            
        if l1:
            p.next = l1
        else:
            p.next = l2
        
        return dummy.next


if __name__ == "__main__":
    pass
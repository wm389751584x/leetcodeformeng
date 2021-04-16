# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if not head or not head.next: return head
        d_small = small = ListNode("inf")
        d_large = large = ListNode("inf")
        
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        small.next = d_large.next
        large.next = None
        return d_small.next

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(5)
    n6 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    r = Solution().partition(n1, 3)
    assert r.to_list() == [1, 2, 2, 4, 3, 5]
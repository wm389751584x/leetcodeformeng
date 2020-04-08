# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next: return head
        dummy, small, large = ListNode(-1), ListNode(-1), ListNode(-1)
        dummy.next = head
        prev, sprev, lprev = dummy, small, large
        
        while prev.next:
            curr = prev.next
            if curr.val < x:
                sprev.next = curr
                sprev = sprev.next
            else:
                lprev.next = curr
                lprev = lprev.next
            prev = prev.next
        lprev.next = None
        sprev.next = large.next
        return small.next


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
        
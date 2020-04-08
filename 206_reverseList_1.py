# Definition for singly-linked list.
# 循环法
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return head
        l, r, q = None, head, head.next

        while q:
            r.next = l
            l = r
            r = q
            q = q.next

        r.next = l
        return r


if __name__ == "__main__":
    pass
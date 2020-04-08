# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n or not head or not head.next:
            return head
        
        dummy = ListNode(0)
        pre = dummy
        dummy.next = head

        for i in range(m - 1):
            pre = pre.next
        
        curr = pre.next

        for i in range(n - m):
            temp = curr.next
            curr.next = temp.next
            temp.next = pre.next
            pre.next = temp
        
        return dummy.next


if __name__ == "__main__":
    pass
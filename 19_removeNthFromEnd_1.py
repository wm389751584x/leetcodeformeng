# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        slow, fast = head, head

        while True:
            while n > 0:
                fast = fast.next
                n -= 1
            if fast == None:
                break
            else:
                pre = slow
                slow = slow.next
                fast = fast.next
        pre.next = slow.next
        slow.next = None
        return dummy.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    s = Solution().removeNthFromEnd(n1, 2)
    assert s.to_list() == [1,2,3,5]
    print('passed all tests')
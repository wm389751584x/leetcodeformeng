# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next: return head
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.sort(l1, l2)

    def sort(self, l1, l2):
        head = ListNode(0)
        node = head
        if not l1: return l2
        if not l2: return l1
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return head.next


if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    print(Solution().sortList(head))
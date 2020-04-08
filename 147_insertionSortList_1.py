# Definition for singly-linked list.
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(-sys.maxsize)
        curr = dummy

        while head:
            if head.val > curr.val:
                temp = head
                head = head.next
                temp.next = curr.next
                curr.next = temp
                curr = curr.next
            else:
                pre = node = dummy
                while node:
                    if head.val <= node.val:
                        temp = head
                        head = head.next
                        temp.next = pre.next
                        pre.next = temp
                        break
                    else:
                        pre = node
                        node = node.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    node = ListNode(4)
    node.next = ListNode(2)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(3)
    print(s.insertionSortList(node))

    
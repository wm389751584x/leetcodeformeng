# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        repeat = False
        while curr.next:
            while curr.next.next and curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
                repeat = True
            if repeat:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()

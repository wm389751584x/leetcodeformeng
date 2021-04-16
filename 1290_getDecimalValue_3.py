# Definition for singly-linked list.
# math way to solve it
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = head.val
        while head := head.next:
            res = res << 1 | head.val
        return res

if __name__ == "__main__":
    pass
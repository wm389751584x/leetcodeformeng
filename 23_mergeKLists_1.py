from typing import List

# Definition for singly-linked list.
# Solution 1: brute force solution
# get all note values into a que
# creating new Notes for each value
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        que = []
        dummy = head = ListNode(0)

        for node in lists:
            while node:
                que.append(node.val)
                node = node.next

        for x in sorted(que):
            dummy.next = ListNode(x)
            dummy = dummy.next
        return head.next


if __name__ == "__main__":
    pass
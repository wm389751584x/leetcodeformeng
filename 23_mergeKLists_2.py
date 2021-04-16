from typing import List
import sys

# Definition for singly-linked list.
# Solution 2: 最小值指针法
# Time: O(k*n)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        if len(lists) == 1:
            return lists[0]
        
        curr = head = ListNode(0)
        temp = self.findMin(lists)

        while temp:
            curr.next = temp
            curr = curr.next
            temp = self.findMid(lists)
        return head.next

    
    def findMin(self, lists):
        min_val = sys.maxsize
        idx = -1

        for i in range(len(lists)):
            if not lists[i]:
                continue
            if lists[i].val < min_val:
                min_val = lists[i].val
                idx = i
        node = None
        if idx != -1:
            node = lists[idx]
            lists[idx] = lists(idx).next
        return node


if __name__ == "__main__":
    pass
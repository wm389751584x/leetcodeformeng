import heapq
from heapq import heappop, heappush

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Heap solution
class Solution():
    def mergeKLists(self, lists):
        """
        type lists: List[ListNode]
        rtype: ListNode
        """
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, [lists[i].val, i])
                lists[i] = lists[i].nexy

        head = p = ListNode()
        while heap:
            v, i = heappop(heap)
            p.next = ListNode(v)
            p = p.next
            if lists[i]:
                heappush(heap, [lists[i].val, i])
                lists[i] = lists[i].next

        return head.next
            
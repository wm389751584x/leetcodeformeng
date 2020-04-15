import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def mergeKLists(self, lists):
        """
        type lists: List[ListNode]
        rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        temp =ListNode(-1)
        head = temp
        while heap:
            snode = heapq.heappop(heap)[-1]
            temp.next = snode
            temp = temp.next
            if snode.next:
                heapq.heappush(head, (snode.next.val, snode.next))
        return head.next
        
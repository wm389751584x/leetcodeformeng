# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # edge case
        if not head: return head

        # setting up pointers
        stack = []
        dummy = cur = ListNode(0)
        dummy.next = head
        pos = cur.next

        while pos:
            for i in range(k):
                if not pos: break
                stack.append(pos)
                pos = pos.next
            
            # check if stack element has enough to play
            if len(stack) < k:
                return dummy.next
            
            while stack:
                cur.next = stack.pop()
                cur = cur.next
            
            # connect the main list
            cur.next = pos

        return dummy.next



if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    node.next.next.next.next.next = None

    print(Solution().reverseKGroup(node, 2))
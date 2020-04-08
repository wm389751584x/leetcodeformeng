# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if not head: return head
        stack = []
        dummy = ListNode(0)
        cur = dummy
        dummy.next = head
        pos = dummy.next
        
        while pos != None:
            for i in range(k):
                if not pos: break
                stack.append(pos)
                pos = pos.next
                
            if len(stack) < k:
                return dummy.next
            
            while len(stack) != 0:
                cur.next = stack.pop()
                cur = cur.next
            
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
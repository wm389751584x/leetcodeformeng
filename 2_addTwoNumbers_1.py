# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Define this to check if it works well
    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        dummy = prev = ListNode(-1)
        dummy.next = l1
        
        carry = 0
        
        while l1 and l2:
            l1.val = l1.val + l2.val + carry
            carry, l1.val = divmod(l1.val, 10)
            prev = l1
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                l1.val += carry
                carry, l1.val = divmod(l1.val, 10)
                prev = l1
                l1 = l1.next
        elif l2:
            prev.next = l2
            l1 = l2
            while l1:
                l1.val += carry
                carry, l1.val = divmod(l1.val, 10)
                prev = l1
                l1 = l1.next
        
        if carry > 0:
            nNode = ListNode(1)
            prev.next = nNode
        
        return dummy.next


if __name__ == "__main__":
    list = ListNode(9)
    list.next = ListNode(9)
    s = Solution().addTwoNumbers(list, ListNode(1))
    assert s.to_list() == [0,0,1]
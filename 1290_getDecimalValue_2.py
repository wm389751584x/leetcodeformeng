# Definition for singly-linked list.
# math way to solve it
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head: return 0
        num = 0
        res = 0

        while head:
            num *= 10
            num += head.val
            head = head.next
        
        dlist = [int(x) for x in str(num)]

        for i in range(len(dlist)):
            d = dlist[-i-1]
            if d:
                res += pow(2, i)
        return res

if __name__ == "__main__":
    pass
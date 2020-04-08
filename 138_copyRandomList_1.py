# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        hashtable = dict()
        curr = head
        while curr:
            hashtable[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            hashtable[curr].next = hashtable[curr.next]
            hashtable[curr].random = hashtable[curr.random]
            curr = curr.next
        
        return hashtable[head]


if __name__ == "__main__":
    pass
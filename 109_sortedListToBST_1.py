# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.convert(nums)

    def convert(self, nums):
        if not nums: return None
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.convert(nums[:mid])
        root.right = self.convert(nums[mid+1:])
        return root
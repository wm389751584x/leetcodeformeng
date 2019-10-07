class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        length = 0
        while head:
            length += 1
            head = head.next

        half1 = length // 2
        half2 = half1
        sum = 0

        if length % 2 == 0:
            half1 -= 1
            while half1 >= 0:
                sum += head.val
                head = head.next
                half1 -= 1
            while half2 >= 0:
                sum -= head.val
                head = head.next
                half2 -= 1
        else:
            while half1 >= 0:
                sum += head.val
                head = head.next
                half1 -= 1
            while half2 >= 0:
                sum -= head.val
                head = head.next
                half2 -= 1

        if sum == 0:
            return True
        else:
            return False

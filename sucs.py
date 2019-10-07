class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        leftBound, rightBound = 0, len(nums) - 1
        stack1 = []
        stack2 = []

        for i in range(len(nums)):
            if not stack1 or nums[i] >= nums[stack1[-1]]:
                stack1.append(i)
            else:
                while nums[i] < nums[stack1[-1]]:
                    leftBound = min(leftBound, stack1.pop())

        for i in range(len(nums) - 1, 0, -1):
            if not stack2 or nums[i] <= nums[stack2[-1]]:
                stack2.append(i)
            else:
                while nums[i] > nums[stack2[-1]]:
                    rightBound = max(rightBound, stack2.pop())

        if rightBound - leftBound > 0:
            return rightBound - leftBound + 1
        else:
            return 0


list = [2, 6, 4, 3, 8]
print Solution().findUnsortedSubarray(list)
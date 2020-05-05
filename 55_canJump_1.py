from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = nums[0]
        for i in range(len(nums)):
            if reach < i:
                return False
            reach = max(reach, nums[i] + i)

        return True
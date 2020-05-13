from typing import List

# 二分法

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        mid = left
        while nums[left] >= nums[right]:
            if left + 1 >= right:
                mid = right
                break
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid
            return nums[mid]

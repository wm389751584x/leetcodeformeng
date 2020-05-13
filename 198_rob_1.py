from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        profit = [0] * len(nums)
        profit[0] = nums[0]
        for i in range(1, len(nums)):
            profit[i] = max(nums[i] + profit[i-2], profit[i-1])
        return profit[-1]
from typing import List
import sys

# 动态规划

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f = g = res = nums[0]
        for i in range(1, n):
            pf, pg = f, g
            f = max(pf * nums[i], nums[i], pg * nums[i])
            g = min(pf * nums[i], nums[i], pg * nums[i])
            res = max(f, res)
        return res
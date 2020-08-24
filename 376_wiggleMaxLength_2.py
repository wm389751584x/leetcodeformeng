from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        inc, dec = [1] * n, [1] * n

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc[i] = dec[i-1] + 1
                dec[i] = dec[i-1]
            elif nums[i] < nums[i-1]:
                inc
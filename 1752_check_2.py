from typing import List, Mapping

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(x > y for x, y in zip(nums, nums[1:])) <= 1
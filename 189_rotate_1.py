from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        while k > 0:
            temp = nums.pop()
            nums.insert(0, temp)


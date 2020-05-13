from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        n = len(nums)
        t1, t2 = nums[:n-k], nums[n-k:]
        nums = t2 + t1


Solution().rotate([1,2,3,4,5,6,7], 3)
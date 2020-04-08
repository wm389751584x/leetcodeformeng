from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        maximum = nums[0]
        dp0, dp1 = nums[0], 0

        for i in range(1, len(nums)):
            dp1 = max(nums[i], dp0 + nums[i])
            dp0 = dp1
            maximum = max(maximum, dp1)

        return maximum


if __name__ == "__main__":
    assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
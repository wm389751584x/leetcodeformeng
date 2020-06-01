from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(map(self.profit, (nums[1:], nums[:-1])))

    def profit(self, nums):
        dp = [0] * (len(nums) + 2)
        for i, num in enumerate(nums, 2):
            dp[i] = max(dp[i-1], dp[i-2] + num)
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.rob([1,2,3,1]) == 4
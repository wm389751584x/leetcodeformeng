from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums: return 0
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)


if __name__ == "__main__":
    assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
from typing import List
# 错误的示范, 这个代码只考虑到了, 之前的全部成立的情况. 
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if (j + 2) % 2 == 0:
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
                else:
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


print(Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
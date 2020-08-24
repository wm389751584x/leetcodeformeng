from typing import List
import time
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num: dp[i] += dp[i-num]
        return dp[-1]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().combinationSum4([4,2,1], 32))
    print("--%s seconds--" % (time.time() - start_time))
from typing import List
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] > amount:
            return -1
        else:
            return dp[-1]


if __name__ == "__main__":
    print(Solution().coinChange([1,2,5], 11))
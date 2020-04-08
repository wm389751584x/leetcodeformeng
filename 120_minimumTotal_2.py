from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = triangle

        for i in range(len(dp)-2, -1, -1):
            for j in range(0, len(dp[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]


if __name__ == "__main__":
    assert Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11
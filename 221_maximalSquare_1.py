from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dp[i+1][j+1] = 0
                else:
                    dp[i+1][j+1] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i][j])


if __name__ == "__main__":
    assert Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4
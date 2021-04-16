from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dynamic programming
        
        row = len(matrix)
        col = len(matrix[0])
        res = 0
        dp = [[1 for _ in range(col)] for _ in range(row)]
        
        
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i - 1 >= 0:
                    if matrix[i][j] > matrix[i-1][j]:
                        dp[i][j] = max(dp[i][j], dp[i-1][j] + 1)
                if i + 1 < row:
                    if matrix[i][j] > matrix[i+1][j]:
                        dp[i][j] = max(dp[i][j], dp[i+1][j] + 1)
                if j - 1 >= 0:
                    if matrix[i][j] > matrix[i][j-1]:
                        dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
                if j + 1 < col:
                    if matrix[i][j] > matrix[i][j+1]:
                        dp[i][j] = max(dp[i][j], dp[i][j+1] + 1)
        res = max(res, max(map(max, dp)))
        print(dp)


if __name__ == "__main__":
    Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])



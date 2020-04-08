from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])

        for i in range(1, n):
            grid[i][0] += grid[i-1][0]

        for j in range(1, m):
            grid[0][j] += grid[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]


if __name__ == "__main__":
    assert Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7
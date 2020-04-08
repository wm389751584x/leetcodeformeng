class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        path = [[1] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[-1][-1]


if __name__ == "__main__":
    assert Solution().uniquePaths(3, 2) == 3
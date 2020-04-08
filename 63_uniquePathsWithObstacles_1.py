from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        path = [[0] * m for _ in range(n)]
        if obstacleGrid[0][0] == 0:
            path[0][0] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                else:
                    if i > 0:
                        path[i][j] += path[i-1][j]
                    if j > 0:
                        path[i][j] += path[i][j-1]
        # print(path)
        
        return path[-1][-1]

if __name__ == "__main__":
    assert Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
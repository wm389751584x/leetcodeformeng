from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        x = len(heights)
        y = len(heights[0])
        dp = [[0 for _ in range(y)] for _ in range(x)]
        
        for i in range(x):
            for j in range(y):
                
                if i > 0 or j > 0:
                    
                    if j == 0:
                        temp = abs(heights[i][j] - heights[i-1][j])
                        if dp[i-1][j] >= temp:
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = temp
                    
                    elif i == 0:
                        temp = abs(heights[i][j] - heights[i][j-1])
                        if dp[i][j-1] >= temp:
                            dp[i][j] = dp[i][j-1]
                        else:
                            dp[i][j] = temp
                    else:
                        up = abs(heights[i][j] - heights[i-1][j]) + dp[i-1][j]
                        left = abs(heights[i][j] - heights[i][j-1]) + dp[i][j-1]

                        if up > left:

                            if left > 2 * dp[i][j-1]:
                                dp[i][j] = left - dp[i][j-1]
                            else:
                                dp[i][j] = dp[i][j-1]
                        elif up < left:
                            if up > 2 * dp[i-1][j]:
                                dp[i][j] = up - dp[i-1][j]
                            else:
                                dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = min(dp[i-1][j], dp[i][j-1])

        print(dp)
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    assert s.minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]) == 5
class Solution:
    def climbStairs(self, n: int) -> int:
        dp0, dp1 = 1, 1
        dpi = 1

        for i in range(2, n+1):
            dpi = dp1 + dp0
            dp0 = dp1
            dp1 = dpi
        
        return dpi


if __name__ == "__main__":
    assert Solution().climbStairs(5) == 8
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * n
        for i in range(1, n-1):
            if A[i-1] + A[i+1] == A[i] * 2:
                dp[i] = dp[i-1] + 1
        return sum(dp)


if __name__ == "__main__":
    assert Solution().numberOfArithmeticSlices([1,2,3,4]) == 3
# dynamic programming
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [0 for _ in range(n)]
        
        for i in range(1, n):
            if s[i] == ')':
                j = i - 1 - dp[i - 1]
                if j >= 0 and s[j] == '(':
                    dp[i] = dp[i-1] + 2
                    if j - 1 >= 0:
                        dp[i] += dp[j-1]
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    s.longestValidParentheses("()(())") == 6
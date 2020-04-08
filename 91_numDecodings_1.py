class Solution:
    def numDecodings(self, s: str) -> int:

        if int(s[0]) == 0:
            return 0

        dp = [0] * (len(s) + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, len(s)+1):
            if int(s[i-1]) != 0:
                dp[i] += dp[i-1]
            if int(s[i-2:i]) <= 26 and int(s[i-2:i]) >= 10:
                dp[i] += dp[i-2]
        
        return dp[-1]


if __name__ == "__main__":
    assert Solution().numDecodings('226') == 3
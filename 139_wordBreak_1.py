from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i, -1, -1):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    continue
        
        return dp[-1]


if __name__ == "__main__":
    assert Solution().wordBreak("leetcode", ["leet","code"]) == True
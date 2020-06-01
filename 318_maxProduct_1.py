from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words: return [0]
        n = len(words)
        dp = [0] * n
        for i in range(n):
            for j in range(i):
                if not set(words[i]) and set(words[j]):
                    dp[i] = max(dp[i], len(words[i]) * len(words[j]))
        return max(dp)


if __name__ == "__main__":
    pass
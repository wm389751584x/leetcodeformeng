from typing import List
from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dp = 0
        d = defaultdict(int)
        n = len(words)
        for i in range(n):
            w = words[i]
            for c in w:
                d[w] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not d[words[i]] & d[words[j]]:
                    dp = max(dp, len(words[i]) * len(words[j]))
        return dp


if __name__ == "__main__":
    pass
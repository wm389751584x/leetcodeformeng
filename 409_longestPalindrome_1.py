from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        prime = 0
        for v in count.values():
            if v % 2 == 1:
                res += v - 1
                prime = 1
            else:
                res += v
        return res + prime


if __name__ == "__main__":
    assert Solution().longestPalindrome("abccccdd") == 7
        
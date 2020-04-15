# dictonary

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        chars = dict()

        for right in range(len(s)):
            if s[right] in chars:
                left = max(left, chars[s[right]] + 1)
            chars[s[right]] = right
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    print('passed all tests')
# swliding windows

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars = []
        res = 0

        while left < len(s) and right < len(s):
            if s[right] in chars:
                chars.remove(s[left])
                left += 1
            else:
                chars.append(s[right])
                right += 1
                res = max(res, len(chars))
        # print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    print('passed all tests')
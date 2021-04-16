# dictonary

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        # dictionary will keep key, val of ( char, idx )
        chars = dict()

        for right in range(len(s)):
            # if right char is alreay in in dictionary
            # then move left window to eigher left idx or right idx + 1
            if s[right] in chars:
                # if current left greater than char in dict
                # then use left
                left = max(left, chars[s[right]] + 1)
            chars[s[right]] = right
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    print('passed all tests')
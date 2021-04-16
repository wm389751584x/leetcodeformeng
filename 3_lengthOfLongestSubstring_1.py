class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if self.isUnique(s[i:j]):
                    maxlen = max(maxlen, len(s[i:j]))
        return maxlen
    
    # check if string contain unique chars
    def isUnique(self, st):
        check = [False] * 128 # 128 full range of ascii table
        for i in range(len(st)):
            val = ord(st[i])
            if check[val]:
                return False
            check[val] = True
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
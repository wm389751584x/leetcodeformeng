class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        while s:
            d = ord(s[0]) - 64
            res += d * (26 ** (len(s) - 1))
            s = s[1:]
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.titleToNumber('ZY') == 701
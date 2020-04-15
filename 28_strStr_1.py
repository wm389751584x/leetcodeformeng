class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle: return -1
        res = -1
        n = len(haystack) - len(needle)
        m = len(needle)
        for i in range(n + 1):
            if haystack[i:i+m] == needle:
                res = i
                break
        return res


if __name__ == "__main__":
    pass
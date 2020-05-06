from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.isPalindrome = lambda s : s == s[::-1]
        res = []
        self.helper(s, res, [])
        return res

    def helper(self, s, res, path):
        if not s:
            res.append(path[:])
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], res, path + [s[:i]])

if __name__ == "__main__":
    s = Solution()
    assert s.partition('aab') == [["a","a","b"],["aa","b"]]
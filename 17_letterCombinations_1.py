from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        lookup = {
            '0': "0",
            '1': "1",
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        return self.dfs(res, '', digits, lookup)
    
    def dfs(self, res, temp, digits, lookup):
        if not digits:
            res.append(temp[:])
            return
        for char in lookup[digits[0]]:
            self.dfs(res, temp+char, digits[1:], lookup)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
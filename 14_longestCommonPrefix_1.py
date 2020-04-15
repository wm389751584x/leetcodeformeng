class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        strs.sort()

        for i in range(len(strs[0])):
            for s in strs:
                if len(s) <= i or strs[0][i] != s[i]:
                    return s[:i]
        return strs[0]


if __name__ == "__main__":
    pass
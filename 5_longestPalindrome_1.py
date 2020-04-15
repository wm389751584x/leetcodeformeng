class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        n = len(s)
        left, right, longest = 0, 0, 0
        ispa = [[False] * n for _ in range(n)]
        for j in range(n):
            ispa[j][j] = True
            for i in range(j):
                if s[i] == s[j] and (j - i <= 1 or ispa[i-1][j+1]):
                    ispa[i][j] = True
                    longest = max(longest, j - i + 1)
                    left = i
                    right = j
        return s[left:right+1]

Solution().longestPalindrome('aabbaa')
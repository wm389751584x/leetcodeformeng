class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = []
        res = s
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u']:
                ans.append(i)
        
        for i in range(len(ans)):
            res = res[:ans[i]] + s[ans[-i-1]] + res[ans[i]+1:]
        return s

Solution().reverseVowels('hello')
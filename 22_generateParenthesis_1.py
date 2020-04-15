from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return []
        res = []
        return self.dfs(n, n, '', res)

    def dfs(self, left, right, temp, res):
        if left == 0 and right == 0:
            res.append(temp[:])
            return
        
        if left > 0:
            self.dfs(left-1, right, temp + '(', res)
        if right > left:
            self.dfs(left, right-1, temp + ')', res)
        
        return res


s = Solution().generateParenthesis(2)
print(s)
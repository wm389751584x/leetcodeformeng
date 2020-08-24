class Solution:
    def lastRemaining(self, n: int) -> int:
        res = [0] * n
        for i in range(1, n+1):
            res[i-1] = i
        
        while len(res) > 1:
            i = 0
            while i < len(res):
                res.pop(i)
                i += 2
            res.reverse()
        
        return res[0]


print(Solution().lastRemaining(9))
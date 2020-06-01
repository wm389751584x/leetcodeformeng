from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(k, n, res, [], 1)
        return res
    
    def dfs(self, k, n, res, temp, idx):
        if len(temp) == k:
            if sum(temp) == n:
                res.append(temp[:])
            return
        
        for i in range(idx, 10):
            self.dfs(k, n, res, temp + [i], i + 1)

print(Solution().combinationSum3(3, 7))
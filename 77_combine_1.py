from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k > n: return res
        self.dfs(n, k, res, [], 1)
        return res

    
    def dfs(self, n, k, res, temp, idx):
        if len(temp) == k:
            res.append(temp[:])
            return
        
        for i in range(idx, n+1):
            temp.append(i)
            self.dfs(n, k, res, temp, i+1)
            temp.pop()

        
if __name__ == "__main__":
    assert Solution().combine(4, 2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
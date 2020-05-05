from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return None
        res = []
        self.dfs(candidates, [], res, target, 0)
        
    def dfs(self, candidates, temp, res, target, idx):
        if sum(temp) > 0:
            return

        if sum(temp) == 0:
            res.append(temp[:])
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, temp + [candidates[i]], res, target, i+1)


if __name__ == "__main__":
    s = Solution()
    s.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]]
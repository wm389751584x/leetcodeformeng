from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        self.dfs(candidates, [], res, target, 0)
        return res

    def dfs(self, candidates, temp, res, target, idx):
        if sum(temp) > target:
            return

        if sum(temp) == target:
            res.append(temp[:])

        for i in range(len(candidates)):
            self.dfs(candidates, temp + [candidates[i]], res, target, i)


if __name__ == "__main__":
    s = Solution()
    s.combinationSum([2,3,6,7], 7) == [[7], [2,2,3]]
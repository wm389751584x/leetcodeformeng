from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        if not nums: return res
        self.dfs(nums, res, [], 0)
        return res

    def dfs(self, nums, res, temp, idx):

        res.append(temp[:])

        for i in range(idx, len(nums)):
            temp.append(nums[i])
            self.dfs(nums, res, temp, i+1)
            temp.pop()


if __name__ == "__main__":
    assert Solution().subsets([1,2,3]) == [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
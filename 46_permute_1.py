from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums: return res
        per = [True] * len(nums)
        self.dfs(nums, per, res, [])
        return res

    def dfs(self, nums, per, res, temp):
        if len(temp) == len(nums):
            res.append(temp[:])
            return

        for i in range(len(nums)):
            if per[i]:
                temp.append(nums[i])
                per[i] = False
                self.dfs(nums, per, res, temp)
                per[i] = True
                temp.pop()


if __name__ == "__main__":
    assert Solution().permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
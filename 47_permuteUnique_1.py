from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, temp):
        if not nums:
            res.append(temp[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.dfs(nums[:i]+nums[i+1:], res, temp)
            temp.pop()


if __name__ == "__main__":
    s = Solution()
    assert s.permuteUnique([1,1,2]) == [[1,1,2],[1,2,1],[2,1,1]]
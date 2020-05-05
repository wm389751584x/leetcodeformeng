from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, temp):
        if temp not in res:
            res.append(temp[:])
            
        for i in range(len(nums)):
            
            self.dfs(nums[i+1:], res, temp + [nums[i]])


if __name__ == "__main__":
    s = Solution()
    assert s.subsetsWithDup([4,4,4,1,4]) == [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
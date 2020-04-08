# 90. Subsets II

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        self.helper(nums, 0, res, [])
        return res
    
    
    def helper(self, nums, idx, res, cur):
        if cur not in res:
            res.append(cur)
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.helper(nums, i+1, res, cur + [nums[i]])


if __name__ == "__main__":
    assert Solution().subsetsWithDup([1,2,2]) == [[],[1],[1,2],[1,2,2],[2],[2,2]]
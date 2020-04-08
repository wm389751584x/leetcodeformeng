from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        if not nums: return res
        
        self.helper(nums, 0, res, [])
        return res

    
    def helper(self, nums, idx, res, cur):
        
        if idx == len(nums):
            res.append(cur)

        else:
            self.helper(nums, idx+1, res, cur)

            cur.append(nums[idx])
            self.helper(nums, idx+1, res, cur)
            cur.pop()


if __name__ == "__main__":
    assert Solution().subsets([1, 2, 3]) == [[],[3],[2],[2,3],[1],[1,3],[1,2],[1,2,3]]
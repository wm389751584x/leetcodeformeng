from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < min(nums): return 0
        if target > max(nums): return len(nums)
        res = 0
        for i in range(len(nums)-1):
            if nums[i] == target:
                res = i
                break
            elif nums[i] < target < nums[i+1]:
                res = i+1
                break
        return res


Solution().searchInsert([1,3],3)
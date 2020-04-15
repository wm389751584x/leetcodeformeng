from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        res = []
        lookup = dict()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                temp = nums[i] + nums[j]
                temp *= -1
                
                if temp in lookup:
                    l = sorted([nums[i], nums[j], nums[lookup[temp]]])
                    res.append(l)
                
                lookup[nums[j]] = j
            lookup.clear()

        return res

if __name__ == "__main__":
    s = Solution()
    s.threeSum([-1,0,1,2,-1,-4])
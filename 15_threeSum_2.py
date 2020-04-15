from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        res = []
        n = len(nums)
        nums.sort()
        
        if nums[0] + nums[1] + nums[2] > 0: return res
        if nums[n-1] + nums[n-2] + nums[n-3] < 0: return res
        
        
        for i in range( n - 2):
            if nums[i] + nums[i+1] + nums[i+2] > 0: break
            left = i + 1
            right = n - 1
            
            while left < right:
                summary = nums[i] + nums[left] + nums[right]
                if summary > 0:
                    right -= 1
                elif summary < 0:
                    left += 1
                else:
                    # once fine the set, need do some clean up
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    s.threeSum([-1,0,1,2,-1,-4])
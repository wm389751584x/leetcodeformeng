from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = sum(nums[:3])
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = sum([nums[i], nums[l], nums[r]])
                if abs(s - target) < abs(res - target):
                    res = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return res

        return res

    
if __name__ == "__main__":
    s = Solution()
    assert s.threeSumClosest([-1,2,1,-4], 1) == 2
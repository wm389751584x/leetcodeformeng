from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        if max(nums) < 0: return 1
        target = 1

        while True:
            if target in nums:
                target += 1
            else:
                return target
                break
    
if __name__ == "__main__":
    s = Solution()
    assert s.firstMissingPositive([0]) == 1
    assert s.firstMissingPositive([-5]) == 1
    assert s.firstMissingPositive([1,2,0]) == 3
    assert s.firstMissingPositive([3,4,-1,1]) == 2
    assert s.firstMissingPositive([7,8,9,11,12]) == 1
    print('passed all tests')
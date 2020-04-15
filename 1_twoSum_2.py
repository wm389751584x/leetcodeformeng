from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i in range(len(nums)):
            if target - nums[i] in lookup:
                return [lookup[target - nums[i]], i]
            else:
                lookup[nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [0,1]
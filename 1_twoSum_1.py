from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2,7,11,15], 9) == [0,1]
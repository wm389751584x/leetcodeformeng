from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        p = 2
        for i in range(2, len(nums)):
            if nums[p-2] != nums[i]:
                nums[p] = nums[i]
                p += 1
        return p


if __name__ == "__main__":
    s = Solution()
    inputs = [1,1,1,2,2,3]
    size = s.removeDuplicates(inputs)
    assert inputs[:size] == [1,1,2,2,3]
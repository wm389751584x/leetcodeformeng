from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge case
        if not nums: return 0
        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        return i + 1 # i is index


if __name__ == "__main__":
    assert Solution().removeDuplicates([1,1,2]) == 2
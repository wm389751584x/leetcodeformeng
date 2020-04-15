from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[j] = nums[i]
            j += 1
        return j


if __name__ == "__main__":
    pass
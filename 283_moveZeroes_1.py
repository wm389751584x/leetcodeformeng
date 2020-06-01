from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0
        
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zeros += 1
            else:
                i += 1
        nums += [0] * zeros
        return nums


if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0,1,0,3,12])
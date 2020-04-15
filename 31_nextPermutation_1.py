from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        target = 0
        change = 0
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                target = i-1
                break

        for i in range(n-1, -1, -1):
            if nums[i] > nums[target]:
                change = i
                break
        
        nums[target], nums[change] =  nums[change], nums[target]

        # check extrame cases

        if target == change == 0:
            nums.reverse()
        else:
            nums[target+1:] = reversed(nums[target+1:])


if __name__ == "__main__":
    pass

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0
        longest = 0
        reach = 0
        for i in range(n):
            if longest < i:
                counter += 1
                longest = reach
            reach = max(reach, nums[i] + i)


if __name__ == "__main__":
    Solution().jump([2,3,1,1,4])
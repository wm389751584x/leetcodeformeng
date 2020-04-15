from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums: return [-1, -1]
        left = right = 0
        for i in range(len(nums)):
            if nums[i] == target:
                right += 1
            else:
                if left == right:
                    left += 1
                    right += 1
                else:
                    break
        return [left, right-1]


if __name__ == "__main__":
    s = Solution()
    assert s.searchRange([5,7,7,8,8,10], 8) == [3, 4]
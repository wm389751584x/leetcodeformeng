from typing import List
import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    s.increasingTriplet([5,1,5,5,2,5,4]) == True
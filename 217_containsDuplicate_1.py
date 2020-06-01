from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = 1
        return False
from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mylist = Counter(nums)
        res = 0
        temp = 0
        for key, val in mylist.items():
            if val > temp:
                res = key
                temp = val
        return res


Solution().majorityElement([3,2,3])
# find element that appear only once. 
from typing import List
import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        clist = collections.Counter(nums)
        for key, val in clist.items():
            if val == 1:
                res.append(key)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([1,2,1,3,2,5]) == [3,5]
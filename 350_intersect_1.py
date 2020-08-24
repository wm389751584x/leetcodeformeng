from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res = []
        for k, v in cnt1.items():
            if k in nums2:
                res += [k] * min(v, cnt2[k])
        return res


if __name__ == "__main__":
    s = Solution()
    s.intersect([4,9,5],[9,4,9,8,4]) == [4,9]
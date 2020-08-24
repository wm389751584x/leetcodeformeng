from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        for num in nums1:
            if num in nums2:
                if num not in res:
                    res.append(num)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.intersection([1,2,2,1],[2,2]) == [2]
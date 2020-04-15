from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        nums = []
        count = 0
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            nums.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            nums.append(nums2[j])
            j += 1
        
        div, mod = divmod(m + n, 2)
        if mod == 0:
            return (nums[div-1] + nums[div]) / 2
        else:
            return nums[div]


if __name__ == "__main__":
    s1 = Solution().findMedianSortedArrays([1,3], [2])
    s2 = Solution().findMedianSortedArrays([1,2], [3,4])

    assert s1 == 2.0
    assert s2 == 2.5

    print('passed all tests')
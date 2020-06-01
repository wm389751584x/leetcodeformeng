from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        n = len(nums)
        for i in range(n):
            res.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(n-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
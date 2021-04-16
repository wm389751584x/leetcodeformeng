from typing import List, Mapping

class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)

        def is_nondec(L):
            return all(x<=y for x, y in zip(L, L[1:]))

        for i in range(N-1):
            if nums[i] > nums[i+1]:
                if is_nondec(nums[i+1:]) and nums[0] >= nums[-1]:
                    return True
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.check([3,4,5,1,2]) == True

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)
        count = 0
        
        for i in range(1, N):
            if nums[i-1]:
                count += 1
                if i == 1:
                    nums[i-1] = nums[i]
                else:
                    if nums[i-2] > nums[i]:
                        nums[i] = nums[i-1]
                    else:
                        nums[i-1] = nums[i]
        print(count)
        return count <= 1


if __name__ == "__main__":
    s = Solution()
    s.checkPossibility([4,2,1])
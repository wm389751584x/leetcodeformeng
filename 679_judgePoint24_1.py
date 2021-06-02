from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def helper(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    status = False

                    x = nums[i]
                    y = nums[j]

                    new_nums = [nums[k] for k in range(len(nums)) if (k != i and k != j)]

                    # 加法
                    if i < j:
                        status = status or helper(new_nums + [x+y])
                        status = status or helper(new_nums + [x*y])
                    # 减法
                    status = status or helper(new_nums + [x-y])
                    # 除法
                    if abs(y) > 1e-6:
                        status = status or helper(new_nums + [x/y])
                    
                    if status:
                        return True
            return False
        
        return helper(nums)


if __name__ == "__main__":
    S = Solution()
    assert S.judgePoint24([1,2,1,2]) == False
    assert S.judgePoint24([4,1,8,7]) == True
from typing import List
import time
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        self.counter = 0
        self.helper([], nums, target)
        return self.counter
    
    def helper(self, temp, nums, target):
        if sum(temp) == target:
            self.counter += 1
        elif sum(temp) > target:
            return
        else:
            for num in nums:
                self.helper(temp + [num], nums, target)
    
if __name__ == "__main__":
    start_time = time.time()
    print(Solution().combinationSum4([4,2,1], 32))
    print("--%s seconds--" % (time.time() - start_time))
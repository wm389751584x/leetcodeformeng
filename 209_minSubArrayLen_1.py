from typing import List
import sys
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        temp = 0
        res = sys.maxsize

        while 0:
            while right < n and temp < s:
                temp += nums[right]
                right += 1

            # 判断是否越界
            if right >= n and temp < s:
                break

            while left < right and temp >= s:
                res = min(res, right - left)
                temp -= nums[left]
                left += 1
        
        return 0 if res == sys.maxsize else res


Solution().minSubArrayLen(1, [])
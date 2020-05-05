from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0
        res = 0
        n = len(height)
        
        temp = height[0]
        left = [0] * n
        for i in range(1, n):
            left[i] = temp
            temp = max(temp, height[i])

        temp = height[n-1]
        right = [0] * n
        for i in range(n-2, -1, -1):
            right[i] = temp
            temp = max(temp, height[i])
        
        for i in range(1, n-1):
            temp = min(left[i], right[i]) - height[i]
            res += temp if temp > 0 else 0
        
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res = 0
        leftmost = rightmost = 0
        i = 0
        j = len(height) - 1
        while i < j:
            leftmost = max(leftmost, height[i])
            rightmost = max(rightmost, height[j])
            if leftmost < rightmost:
                res += leftmost - height[i]
                i += 1
            else:
                res += rightmost - height[j]
                j -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
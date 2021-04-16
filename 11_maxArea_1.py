class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) <= 1: return 0
        res = 0
        curr, maxv = 0, 0
        i, j = 0, len(height) - 1
        while i < j:
            curr = min(height[i], height[j]) * (j - i)
            maxv = max(maxv, curr)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxv


if __name__ == "__main__":
    pass
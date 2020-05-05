class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                return mid
        return left - 1


if __name__ == "__main__":
    s = Solution()
    assert s.mySqrt(6) == 2
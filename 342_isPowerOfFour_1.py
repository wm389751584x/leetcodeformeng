class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0: return False
        while num % 4 == 0:
            num /= 4
        return num == 1


if __name__ == "__main__":
    s = Solution()
    s.isPowerOfFour(16) == True
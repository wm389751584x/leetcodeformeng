class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # 判断二进制中不存在奇数为为1
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 != 0


if __name__ == "__main__":
    s = Solution()
    s.isPowerOfFour(16) == True
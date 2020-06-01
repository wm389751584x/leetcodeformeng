# add all digits until there is only one digit
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(d) for d in str(num)])
        return num


if __name__ == "__main__":
    s = Solution()
    assert s.addDigits(38) == 2
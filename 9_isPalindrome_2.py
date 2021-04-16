class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        y = int("".join(reversed(str(x))))


if __name__ == "__main__":
    s = Solution()
    s.isPalindrome(-123)
    # assert s.isPalindrome(123) == False
    # assert s.isPalindrome(121) == True
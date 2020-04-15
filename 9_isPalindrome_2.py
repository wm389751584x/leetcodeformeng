class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        y = int(''.join(reversed([x for x in str(x)])))
        return x == y


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(123) == False
    assert s.isPalindrome(121) == True
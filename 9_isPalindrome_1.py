class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x // 10 == 0: return True
        if x < 0: return False

        # converting int to array
        num = [int(x) for x in str(x)]
        i, j = 0, len(num) - 1

        while i < j:
            if num[i] != num[j]: return False
            i += 1
            j -= 1
        
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(123) == False
    assert s.isPalindrome(121) == True
class Solution:
    def compareProduct(self, num: int):
        if num < 10:
            return False
        oddProdValue, evenProdValue = 0, 0
        while num > 0:
            digit = num % 10
            oddProdValue += digit
            num = num // 10
            if num == 0:
                break
            digit = num % 10
            evenProdValue += digit
            num = num // 10

        if oddProdValue == evenProdValue:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    # print(s.compareProduct(110))
    assert s.compareProduct(11) == True
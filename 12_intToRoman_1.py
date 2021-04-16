class Solution:
    def intToRoman(self, num: int) -> str:
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        roman = ''

        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman += numerals[i]
        return roman


if __name__ == "__main__":
    s = Solution()
    assert s.intToRoman(9) == "IX"
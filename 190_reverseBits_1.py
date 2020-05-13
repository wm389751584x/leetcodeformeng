class Solution:
    def reverseBits(self, n: int) -> int:
        temp = bin(n).replace('0b', '')
        while len(temp) < 32:
            temp = '0' + temp
        temp = temp[::-1]
        return int(temp, 2)


if __name__ == "__main__":
    s = Solution()
    assert s.reverseBits()
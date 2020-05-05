class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]


if __name__ == "__main__":
    s = Solution()
    assert s.addBinary('11', '1') == '100'
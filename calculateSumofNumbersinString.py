class Solution:
    def calculateSumofNumbersinString(self, inputString: str) -> int:
        temp = '0'
        sum = 0
        N = len(inputString)

        for i in range(N):
            ch = inputString[i]
            if ch.isdigit():
                temp += ch
            else:
                sum += int(temp)
                temp = '0'
        return sum + int(temp)


if __name__ == "__main__":
    s = Solution()
    assert s.calculateSumofNumbersinString("1abc23") == 24
    assert s.calculateSumofNumbersinString("geeks4geeks") == 4
    assert s.calculateSumofNumbersinString("1abc2x30yz67") == 100
    assert s.calculateSumofNumbersinString("123abc") == 123
    
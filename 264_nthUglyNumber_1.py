# find nth ugly number
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.nthUglyNumber()
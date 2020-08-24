class Solution:
    def getMoneyAmount(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l < r:
            mid = l + (r-l)//2
            res += mid
            l = mid + 1
        return res


if __name__ == "__main__":
    s = Solution()
    s.getMoneyAmount(10)
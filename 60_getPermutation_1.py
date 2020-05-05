class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        fact = 1
        for i in range(1, n): fact *= i
        res = []
        array = list(range(1, n+1))

        for i in range(n-1, 0, -1):
            idx = k // fact
            res.append(str(array[idx]))
            array = array[:idx] + array[idx+1:]
            k %= fact
            fact //= i
        res.append(str(array[0]))
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    assert s.getPermutation(4, 9) == '2314'
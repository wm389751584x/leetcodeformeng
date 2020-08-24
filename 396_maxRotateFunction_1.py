from typing import List
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        _sum = 0
        n = len(A)
        f = 0
        for i, a in enumerate(A):
            _sum += a
            f += i * a
        res = f
        for i in range(n-1, 0, -1):
            f = f + _sum - n * A[i]
            res = max(res, f)
        return res


if __name__ == "__main__":
    assert Solution().maxRotateFunction([4, 3, 2, 6]) == 26
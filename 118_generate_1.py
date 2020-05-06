from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            res.append(temp)
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j] + res[i-1][j-1]
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
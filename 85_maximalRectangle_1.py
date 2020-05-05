from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        n = len(matrix[0])
        res = 0
        heights = [0 for _ in range(n + 1)]

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    s.maximalRectangle([["1","0","1","0","0"],\
                        ["1","0","1","1","1"],\
                        ["1","1","1","1","1"],\
                        ["1","0","0","1","0"]]) == 6
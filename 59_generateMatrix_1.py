from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0: return []
        res = [[0] * n for _ in range(n)]
        
        counter = 1
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        while left < right and top < bottom:
            # four loops to munipulate the matrix
            for i in range(left, right):
                res[top][i] = counter
                counter += 1

            for i in range(top, bottom):
                res[i][right] = counter
                counter += 1

            for i in range(right, left, -1):
                res[bottom][i] = counter
                counter += 1
            
            for i in range(bottom, top, -1):
                res[i][left] = counter
                counter += 1

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        if n % 2 != 0:
            res[n//2][n//2] = counter
        
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]]
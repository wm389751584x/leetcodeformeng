# 74. Search a 2D Matrix

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        l, h = 0, m * n - 1

        while l <= h:
            mid = l + (h - l) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                h = mid - 1
            else:
                l = mid + 1
        
        return False


if __name__ == "__main__":
    assert Solution().searchMatrix([[1]], 1) == True
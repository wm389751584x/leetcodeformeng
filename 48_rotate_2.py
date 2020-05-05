from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix: return []
        n = len(matrix)

        for i in range(n):
            for j in range(n-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][n-i-1]
                matrix[n-j-1][n-i-1] = temp
        
        for i in range(n // 2):
            matrix[i] = matrix[n-i-1]
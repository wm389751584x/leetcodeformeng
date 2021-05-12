from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # bruceforce

        total = 0

        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                total += self.matrix[i][j]

        return total


if __name__ == "__main__":
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(2, 1, 4, 3) == 8

        
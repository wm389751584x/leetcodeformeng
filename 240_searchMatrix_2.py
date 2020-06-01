class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        rows = len(matrix)
        cols = len(matrix)
        row, col = rows - 1, 0
        while True:
            if row >= 0 and col < cols:
                if matrix[row][col] < target:
                    col += 1
                elif matrix[row][col] > target:
                    row -= 1
                else:
                    return True                    
            else:
                return False


if __name__ == "__main__":
    pass
from typing import List
import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        res = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                total = self.calculate(board, i, j)
                if board[i][j] == 1:
                    if total < 2:
                        res[i][j] = 0
                    if 2 <= total <= 3:
                        res[i][j] = 1
                    if total > 3:
                        res[i][j] = 0
                else:
                    if total == 3:
                        res[i][j] = 1
        board = res
    
    def calculate(self, board, i, j):
        total = 0
        if i > 0:
            total += board[i-1][j]
        if i < len(board)-1:
            total += board[i+1][j]
        if j > 0:
            total += board[i][j-1]
        if j < len(board[0])-1:
            total += board[i][j+1]
        if i > 0 and j > 0:
            total += board[i-1][j-1]
        if i < len(board)-1 and j < len(board[0])-1:
            total += board[i+1][j+1]
        if i > 0 and j < len(board[0])-1:
            total += board[i-1][j+1]
        if i < len(board)-1 and j > 0:
            total += board[i+1][j-1]
        return total


if __name__ == "__main__":
    s = Solution()
    s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return 
        queue = []
        n = len(board)
        m = len(board[0])

        # push edge O into queue
        for i in range(n):
            for j in range(m):
                if ((i in (0, n-1)) or (j in (0, m-1))) and board[i][j] == 'O':
                    queue.append((i, j))

        # seach inside queue
        while queue:
            p, q = queue.pop(0)
            if 0 <= p < n and 0 <= q < m and board[p][q] == 'O':
                board[p][q] = 'M'
                if p - 1 >= 0 and board[p-1][q] == 'O':
                    queue.append((p-1, q))
                if p + 1 < n and board[p+1][q] == 'O':
                    queue.append((p+1, q))
                if q - 1 >= 0 and board[p][q-1] == 'O':
                    queue.append((p, q-1))
                if q + 1 < m and board[p][q+1] == 'O':
                    queue.append((p, q+1))
        
        # clean up the board
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    expected_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    Solution().solve(board)
    assert board == expected_board
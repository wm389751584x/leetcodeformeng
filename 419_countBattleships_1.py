from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        def is_valid(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            else:
                return True

        def dfs(i, j):
            if not is_valid(i, j): return
            elif board[i][j] == '.': return
            else:
                board[i][j] = '.'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        if not board: return
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    res += 1
                    dfs(i, j)
        return res


if __name__ == "__main__":
    assert Solution().countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])\
        == 2
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check for each row
        for row in range(9):
            taken = [False] * 9
            for i in range(9):
                c = board[i][row]
                if c != '.':
                    num = int(c) - 1
                    if taken[num] == True: return False
                    else: taken[num] = True

        # check for each column
        
        # checkf or each 3*3 box
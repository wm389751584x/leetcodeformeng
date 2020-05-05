class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check for each row
        for row in range(9):
            taken = [False] * 9
            for i in range(9):
                c = board[i][row]
                if c != '.':
                    num = int(c) - 1
                    if taken[num] == True: 
                        return False
                    else: 
                        taken[num] = True

        # check for each column
        for col in range(9):
            taken = [False] * 9
            for i in range(9):
                c = board[col][i]
                if c != '.':
                    num = int(c) - 1
                    if taken[num] == True: 
                        return False
                    else:
                        taken[num] = True

        # checkf or each 3*3 box
        for box in range(9):
            taken = [False] * 9
            for row in range(3):
                for col in range(3):
                    c = board[col + 3 * (box//3)][row + 3 * (box % 3)]
                    if c != '.':
                        num = int(c) - 1
                        if taken[num] == True:
                            return False
                        else:
                            taken[num] = True

        return True
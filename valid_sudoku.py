class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if not board: return False
        dict1 = {}
        dict2 = {}
        
        i, j = 0, 0
        
        for i in range(9):
            for j in range(9):
                if board[i][j] not in dict1:
                    dict1[board[i][j]] = 1
                if board[j][i] not in dict2:
                    dict2[board[j][i]] = 1
                else:
                    return False
            dict1.clear()
            dict2.clear()
            
        
        for i in range(3):
            for j in range(3):
                if board[i][j] not in dict1:
                    dict1[board[i][j]] == 1
                else:
                    return False
        dict1.clear()  
        
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] not in dict1:
                    dict1[board[i][j]] == 1
                else:
                    return False
        dict1.clear()
        
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] not in dict1:
                    dict1[board[i][j]] == 1
                else:
                    return False
        dict1.clear()    
        
        for i in range(3):
            for j in range(3, 6):
                if board[i][j] not in dict1:
                    dict1[board[i][j]] == 1
                if board[i][j] not in dict2:
                    dict1[board[i][j]] == 1
                else:
                    return False
        dict1.clear()
        dict2.clear()
            
        for i in range(3):
            for j in range(6, 9):
                if board[i][j] not in dict1:
                    dict1[board[i][j]] == 1
                if board[i][j] not in dict2:
                    dict1[board[i][j]] == 1
                else:
                    return False
        dict1.clear()
        dict2.clear()
        
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] not in dict1:
                    dict1[board[i][j]] == 1
                if board[i][j] not in dict2:
                    dict1[board[i][j]] == 1
                else:
                    return False
        dict1.clear()
        dict2.clear()
        
        return True

if __name__ == "__main__":
    assert Solution().isValidSudoku() == 
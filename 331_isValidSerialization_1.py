class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        prelist = preorder.split(',')

        n = 1
        for c in prelist:
            n -= 1
            if n < 0: return False
            if c == '#':
                pass
            else:
                n += 2
        if n == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    assert Solution().isValidSerialization("7,2,#,2,#,#,#,6,#") == False
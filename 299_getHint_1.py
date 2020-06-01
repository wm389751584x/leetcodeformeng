class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        i = 0
        secret = [int(d) for d in secret]
        guess = [int(d) for d in guess]
        while i < len(secret):
            if secret[i] == guess[i]:
                bull += 1
                secret.pop(i)
                guess.pop(i)
            else:
                i += 1
        
        for i in range(len(secret)):
            if guess[i] in secret:
                cow += 1
        
        return str(bull) + 'A' + str(cow) + 'B'
        
        
if __name__ == "__main__":
    # assert Solution().getHint('1123', '0111') == '1A1B'
    assert Solution().getHint("1807", "7810") == "1A3B"
      
        
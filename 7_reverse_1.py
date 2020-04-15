class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        
        nage = False
        res = 0
        if x < 0: 
            nage = True
            x *= -1
        
        while x % 10 == 0:
            x //= 10
        
        while x != 0:
            res += x % 10
            x //= 10
            if x > 0:
                res *= 10
        
        if nage:
            res *= -1
        if res < -2**31 or res > 2**31-1: return 0
        return res
        

if __name__ == "__main__":
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(1563847412) == 0
    print('passed all tests')
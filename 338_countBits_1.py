# brute force
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            n = i
            count = 0
            while n:
                count += n & 1
                n >>= 1
        return res

    
if __name__ == "__main__":
    pass
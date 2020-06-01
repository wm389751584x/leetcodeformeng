# check is a number is ugly number
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        elif num <= 0:
            return False

        if num % 2 == 0:
            return self.isUgly(num / 2)
        elif num % 3 == 0:
            return self.isUgly(num / 3)
        elif num % 5 == 0:
            return self.isUgly(num / 5)
        else:
            return False
    

if __name__ == "__main__":
    s = Solution()
    s.isUgly(6) == True
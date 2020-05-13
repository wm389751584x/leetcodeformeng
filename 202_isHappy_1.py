class Solution:
    def isHappy(self, n: int) -> bool:
        d = dict()
        while n not in d:
            if n == 1: return True
            d[n] = True
            temp = 0
            while True:
                div, mod = divmod(n, 10)
                temp += pow(mod, 2)

                if div == 0:
                    break
                else:
                    n = div
            n = temp
        return False
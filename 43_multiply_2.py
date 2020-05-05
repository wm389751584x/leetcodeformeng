class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = list(num1)
        num2 = list(num2)
        num1.reverse()
        num2.reverse()
        
        res = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1)):
            div, mod = 0, 0
            for j in range(len(num2)):
                temp = int(num1[i]) * int(num2[j])
                mod = temp % 10
                div = temp // 10
                res[i+j] += mod
                if div:
                    res[i+j+1] += div

        
        for i in range(len(res)-1):
            if res[i] >= 10:
                div, mod = divmod(res[i], 10)
                res[i] = mod
                res[i+1] += div
        
        res.reverse()
        a = ''.join(str(ele) for ele in res)
        return a.lstrip('0')        


if __name__ == "__main__":
    Solution().multiply('123','456') == '56088'
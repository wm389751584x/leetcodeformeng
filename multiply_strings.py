class Solution:
    def multiply(self, num1, num2):
        
        retval = 0
        
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            take = 0
            passval = 0
            for j in range(len(num2)-1, -1, -1):
                value = int(num1[j]) * int(num2[i])
                value += carry
                carry = value // 10
                take = value % 10

                take = (10 ** (len(num1) - j - 1)) * take
                passval += take
            retval += (10 ** (len(num1) - i - 1)) * passval
            
        return str(retval)

print(Solution().multiply('123', '456'))
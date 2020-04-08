# 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        if len(num1) == 0 or len(num2) == 0: return '0'
        
        # reverse two list
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        len1 = len(num1)
        len2 = len(num2)
        
        # max length of resume will be len1 + len2
        # so create a resume of len1 + len2
        arr = [ 0 for i in range(len1 + len2)]
        
        for i in range(len1):
            for j in range(len2):
                mul = int(num1[i]) * int(num2[j])
                poslow = i + j
                poshigh = i + j + 1
                mul += arr[poslow]
                arr[poslow] = mul % 10
                arr[poshigh] += mul//10
                
        res = []
        
        for i in range(len(arr)):
            res.insert(0, str(arr[i]))
            
        while res[0] == '0' and len(res) > 1:
            del res[0]
            
        return ''.join(res)
        

if __name__ == "__main__":
    assert Solution().multiply("120", "20000") == "2400000"
    assert Solution().multiply("0", "3421") == "0"
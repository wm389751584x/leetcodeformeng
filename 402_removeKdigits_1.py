class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if len(num) == k:
            return '0'

        stack = []
        
        # if current digit > next digit, delete it. 
        # also 
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        
        # if k > 0
        while k > 0:
            stack.pop()
            k -= 1
        
        # clear leading zero
        while len(stack) > 1 and stack[0] == '0':
            stack.pop(0)
        
        return ''.join(stack)


if __name__ == "__main__":
    # assert Solution().removeKdigits('1432219',3) == '1219'
    assert Solution().removeKdigits("1234567890",9) == '0'
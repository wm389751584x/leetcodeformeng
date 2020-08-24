class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digit = 0
        temp = ''
        res = ''
        instack = False
        for c in s:
            if c.isdigit():
                instack = True
            elif c == ']':
                instack = False
                while stack[-1] != '[':
                    temp += stack.pop()
                stack.pop()
                digit = stack.pop()
                res += digit * temp
            if instack:
                stack.append(c)
            else:
                res += c
        return res


print(Solution().decodeString("3[a]2[bc]"))
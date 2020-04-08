class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        num = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = c
                num = 0
        return sum(stack)

if __name__ == "__main__":
    assert Solution().calculate("3+2*10") == 23
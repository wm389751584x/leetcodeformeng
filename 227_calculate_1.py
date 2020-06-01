class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if i == len(s) - 1 or c in ['+', '-', '*', '/']:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                num = 0
                sign = c
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.calculate("14-3/2") == 13
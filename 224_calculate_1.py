class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ['-', '+']:
                res = res + sign * num
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res = res + sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign * num
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.calculate('1 - ( 1 + 1)') == -1
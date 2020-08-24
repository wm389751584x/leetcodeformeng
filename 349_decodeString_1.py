class Solution:
    def decodeString(self, s: str) -> str:
        curnum = 0
        curstring = ''
        stack = []
        for c in s:
            if c == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif c == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum * curstring
            elif c.isdigit():
                curnum = curnum * 10 + int(c)
            else:
                curstring += c
        return curstring


if __name__ == "__main__":
    assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
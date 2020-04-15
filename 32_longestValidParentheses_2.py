# stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack = []
        maxval = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    stack.append(i)
                else:
                    if stack[-1] == '(':
                        stack.pop()
                        if not stack:
                            temp = i + 1
                            maxval = max(maxval, temp)
                        else:
                            temp = i - stack[-1]
                            maxval = max(maxval, temp)
                    else:
                        stack.append(i)
        return maxval



if __name__ == "__main__":
    s = Solution()
    s.longestValidParentheses("()(())") == 6
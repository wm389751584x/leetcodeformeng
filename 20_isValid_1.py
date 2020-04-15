class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif stack:
                temp = stack[-1]
                if temp == lookup[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return stack == []

    
if __name__ == "__main__":
    s = Solution()
    s.isValid('()') == True
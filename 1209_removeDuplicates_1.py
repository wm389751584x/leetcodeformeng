class Solution:
    # manual 
    def removeDuplicates(self, s: str, k: int) -> str:
        N = len(s)
        if N < k or not s: return s
        
        stack = []
        res = ""

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] >= k: stack.pop()
                continue
            stack.append([c, 1])
        
        for val, cnt in stack:
            res += val * cnt
        
        return res


if __name__ == 
import sys
import traceback
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


if __name__ == "__main__":
    s = Solution()
    try:
        assert s.removeDuplicates("acbbccc",2) == "b"
    # many more statements like this
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))
        exit(1)

try:
    assert s.removeDuplicates() == 
except AssertionError:
    _, _, tb = sys.exc_info()
    traceback.print_tb(tb) # Fixed format
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]

    print('An error occurred on line {} in statement {}'.format(line, text))
    exit(1)
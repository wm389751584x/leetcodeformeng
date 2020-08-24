# deque
import collections

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = collections.deque(s)
        for c in t:
            if c == queue[0]:
                queue.popleft()
        return not queue


if __name__ == "__main__":
    print(Solution().isSubsequence("aaaaaa", "bbaaaa"))
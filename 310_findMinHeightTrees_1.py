from typing import List
import collections
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        d = collections.defaultdict(list)
        for key, val in edges:
            d[key].append(val)
            d[val].append(key)

        que = deque()
        
        for key, vals in d:
            if len(vals) == 1:
                que.append(key)
        
        while n > 2:
            l = len(que)
            n -= l
            for _ in range(l):
                key = que.popleft()
                for val in d[key]:
                    d[val].remove(key)
                    if len(d[val]) == 1:
                        que.append(val)
        return list(que)


if __name__ == "__main__":
    pass
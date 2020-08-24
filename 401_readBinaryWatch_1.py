from typing import List
from itertools import combinations
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        self.dfs(num, 0, res)
        return res

    def dfs(self, num, hours, res):
        if hours > num: return
        for hour in combinations([1,2,4,8], hours):
            hs = sum(hour)
            if hs >= 12: continue
            for minu in combinations([1,2,4,8,16,32], num - hours):
                ms = sum(minu)
                if ms >= 60: continue
                res.append("%d:%02d" % (hs, ms))
        self.dfs(num, hours + 1, res)

        
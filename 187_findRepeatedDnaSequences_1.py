from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        n = len(s)
        for i in range(n):
            cur = s[i : i + 10]
            if cur in seen:
                res.add(cur)
            else:
                seen.add(cur)
        return list(res)

Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
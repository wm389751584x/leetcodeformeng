from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: return []
        res = []
        intervals = sorted(intervals, key = lambda l:l[0])
        for i in intervals:
            if res and i[0] < res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], i[-1])
            else:
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        res = []
        intervals = sorted(intervals, key=lambda x:x[0])
        for i in intervals:
            if res and i[0] < res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], i[-1])
            else:
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.insert([[1,3],[6,9]],[2,5]) == [[1,5],[6,9]]
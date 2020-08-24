from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s_map = {v[0] : i for i, v in enumerate(intervals)}
        s_list = [i[0] for i in intervals]
        res = []
        s_list.sort()
        for interval in intervals:
            pos = self.finder(s_list, interval[-1])
            res.append(s_map[s_list[pos]] if pos != -1 else -1)
        return res
            
        
    def finder(self, s_list, val):
        lo, hi = 0, len(s_list) - 1
        res = -1
        while hi >= lo:
            mid = lo + (hi - lo) // 2
            if s_list[mid] >= val:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
                

if __name__ == "__main__":
    pass
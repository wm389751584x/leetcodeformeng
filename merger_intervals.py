class Solution:
    def merge(self, intervals):
        
        if not intervals: return []
        
        out = []
        
        intervals = sorted(intervals, key = lambda l:l[0])
        
        for i in intervals:
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else:
                out.append(i)
                
        return out


testcase = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(testcase))
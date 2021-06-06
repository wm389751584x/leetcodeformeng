from typing import List


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        maxhigh = 0
        def helper(box, high):
            size = len(box)
            if size == 1:
                return box[0][-1] + high
            
            for i in range(size):
                for j in range(size):

                    if i == j: 
                        continue

                    if box[j][0] > box[i][0] and box[j][1] > box[i][1] and box[j][-1] > box[i][-1]:
                        high += box[j][-1]
                        remain = [box[_] for _ in range(size) if _ != j]
                        maxhigh = max(helper(remain, high), maxhigh)
                        high -= box[j][-1]
        return maxhigh
                    

if __name__ == "__main__":
    Solution().pileBox([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
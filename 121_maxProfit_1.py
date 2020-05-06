from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        lowp = sys.maxsize
        maxp = 0

        for i in prices:
            lowp = min(lowp, i)
            maxp = max(maxp, i - lowp)

        return maxp


if __name__ == "__main__":
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
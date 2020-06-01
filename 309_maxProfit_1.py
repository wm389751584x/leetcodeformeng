from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 状态鸡
        held = -sys.maxsize
        sold = -sys.maxsize
        cool = 0
        for p in prices:
            preSold = sold
            sold = held + p
            held = max(held, cool - p)
            cool = max(cool, preSold)
        return max(sold, cool)


if __name__ == "__main__":
    s = Solution()
    # print(s.maxProfit([1,2,3,0,2]))
    assert s.maxProfit([1,2,3,0,2]) == 3
from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for line in matrix:
            nums.extend(line)
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        return res


if __name__ == "__main__":
    Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8) == 13
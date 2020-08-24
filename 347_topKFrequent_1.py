from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, val in Counter(nums).most_common(k)]


if __name__ == "__main__":
    s = Solution()
    s.topKFrequent([1,1,1,2,2,3], 2) == [1, 2]
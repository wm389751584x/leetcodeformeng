from typing import List
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i, v in enumerate(nums):
            self.d[v].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])


if __name__ == "__main__":
    s = Solution()

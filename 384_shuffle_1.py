from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        num = self.nums[:]
        random.shuffle(num)
        return num


if __name__ == "__main__":
    pass
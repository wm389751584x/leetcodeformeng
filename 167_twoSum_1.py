from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in d:
                return sorted([i+1, d[temp]+1])
            else:
                d[numbers[i]] = i
        

if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2,7,11,15],9) == [1,2]
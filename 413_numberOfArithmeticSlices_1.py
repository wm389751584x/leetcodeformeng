from typing import List
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        total = 0
        i = 0
        while i < len(A):
            count = 0
            while i+2 < len(A) and A[i+1] - A[i] == A[i+2] - A[i+1]:
                count += 1
                total += count
                i += 1
            i += 1
            
        return total


if __name__ == "__main__":
    Solution().numberOfArithmeticSlices([1, 3, 5, 7, 9]) == 3

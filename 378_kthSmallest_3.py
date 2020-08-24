from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            cnt = self.search(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left
    
    def search(self, matrix, target):
        n = len(matrix)
        i, j = n - 1, 0
        res = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                res += i + 1
                j += 1
            else:
                i -= 1
        return res


if __name__ == "__main__":
    Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8) == 13
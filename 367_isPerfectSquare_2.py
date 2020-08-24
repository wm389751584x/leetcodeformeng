# binary search
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num + 1
        while l < r: 
            mid = l + (r - l) // 2
            if num[mid] == 
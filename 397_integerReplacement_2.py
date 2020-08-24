class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            count += 1
            if n & 1: # odd
                if n & 2 and n != 3:
                    n += 1
                else:
                    n -= 1
            else:
                n >>= 1
        return count


if __name__ == "__main__":
    assert Solution().integerReplacement(7) == 4
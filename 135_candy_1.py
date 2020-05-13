from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        ratings.reverse()

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i], candies[i-1] + 1)

        return sum(candies)


if __name__ == "__main__":
    s = Solution()
    assert s.candy([1,0,2]) == 5
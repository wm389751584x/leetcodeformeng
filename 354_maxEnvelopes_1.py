from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        dp = [1] * len(envelopes)

        for i in range(len(envelopes)):
            for j in range(i):

                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[j] += 1
                
        return max(dp)


if __name__ == "__main__":
    assert Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3
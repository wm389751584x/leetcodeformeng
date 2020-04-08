from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost): return -1
        remain = 0
        start = 0

        for i in range(len(gas)):
            if gas[i] - cost[i] + remain < 0:
                start = i + 1
                remain = 0
            else:
                remain += gas[i] - cost[i]

        return start
        

if __name__ == "__main__":
    assert Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
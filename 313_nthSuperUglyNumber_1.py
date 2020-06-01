from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        stp = [0] * len(primes)
        primes.sort()
        
        while len(ugly) < n:
            for i in range(len(stp)):
                while ugly[stp[i]] * primes[i] <= ugly[-1]:
                    stp[i] += 1
            res = [primes[i] * ugly[stp[i]] for i in range(len(primes))]
            ugly.append(min(res))
        print(ugly)
        return ugly[-1]



Solution().nthSuperUglyNumber(12, [2,7,13,19])
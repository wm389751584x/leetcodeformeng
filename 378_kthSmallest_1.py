# numpy
from typing import List
import numpy as np 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = np.array(matrix)
        res = res.flatten()
        res.sort()
        return res[k-1]
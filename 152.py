from typing import List
from math import inf

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos = -1
        neg = 0
        maxp = -inf
        for x in nums:
            if x == 0:
                pos = 0
                neg = 0
            elif x > 0:
                pos = max(x, pos * x) if pos > 0 else x
                neg = neg * x
            else:
                pos1 = neg * x
                neg = min(pos * x, x)
                pos = pos1
            maxp = max(maxp, pos, neg)
        return maxp
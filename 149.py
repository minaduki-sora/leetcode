from typing import List
from math import inf, sqrt
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        ans = 0

        for i, (x1, y1) in enumerate(points):
            linedict = defaultdict(int)
            for j in range(i+1, n):
                x2, y2 = points[j]
                if x1 == x2:
                    k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = y1 - k * x1
                hk = (k, b)
                linedict[hk] += 1
            ans = max(ans, linedict.values())
         
        return ans
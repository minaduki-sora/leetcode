from typing import List
from collections import defaultdict

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        irrigation = defaultdict(int)
        for i, r in enumerate(ranges):
            left = i-r if i-r > 0 else 0
            right = i+r
            irrigation[left] = max(irrigation[left], right)
        d=0
        nxt=0
        cnt=0
        for i in range(n+1):
            if i > d:
                return -1
            nxt=max(nxt, irrigation[i])
            if i==n:
                return cnt
            if i == d:
                cnt+=1
                d=nxt
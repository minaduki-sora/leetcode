from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        lh = []
        vol = 0
        hs = len(height)
        maxh = 0
        for i in range(0, hs):
            maxh = max(maxh, height[i])
            lh.append(maxh)
        maxh = 0
        for i in reversed(range(0, hs)):
            maxh = max(maxh, height[i])
            vol += min(lh[i], maxh) - height[i]
        return vol
        
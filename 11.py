from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                vol = max(vol, height[left] * (right - left))
                left += 1
            else:
                vol = max(vol, height[right] * (right - left))
                right -= 1
        return vol
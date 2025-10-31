from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        d = 0
        for i, x in enumerate(nums):
            if i > d:
                return False
            d = max(d, i+x)
            if d >= n-1:
                return True
        return True
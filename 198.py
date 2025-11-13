from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        f0, f1, f2, f3 = 0, 0, 0, 0
        for x in nums:
            f3 = max(f0 + x, f1 + x)
            f0, f1, f2 = f1, f2, f3
        return max(f0, f1, f2)

    def rob(self, nums: List[int]) -> int:
        f0, f1 = 0, 0
        for x in nums:
            f1 = max(f1, f0 + x)
            f0 = f1
        return f1

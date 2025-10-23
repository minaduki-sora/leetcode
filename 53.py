from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        ans = -1e5
        for x in nums:
            sums += x
            ans = max(ans, sums)
            if sums < 0:
                sums = 0
        return ans
                

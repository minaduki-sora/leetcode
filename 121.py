from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        ans = 0
        for i, x in enumerate(prices):
            if x <= prices[left]:
                left = i
            ans = max(ans, x - prices[left])
        return ans
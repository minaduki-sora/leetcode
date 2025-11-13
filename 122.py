from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = 0
        for i in range(1, n):
            dp += max(0, prices[i] - prices[i-1])
        return dp
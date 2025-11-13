from typing import List
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [-1] * amount
        for i in range(1, amount+1):
            f = [1 + dp[i-coin] for coin in coins if i >= coin and dp[i-coin] != -1]
            dp[i] = min(f) if f else -1
        
        return dp[amount]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] < inf else -1
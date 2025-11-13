from typing import List
from math import inf

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [[[-inf] * 2 for _ in range(k+2)] for _ in range(n+1)]
        for j in range(k+2):
            f[0][j][0] = 0
        for i, p in enumerate(prices):
            for j in range(k+1):
                f[i+1][j+1][0] = max(f[i][j+1][0], f[i][j][1] + p)
                f[i+1][j+1][1] = max(f[i][j+1][1], f[i][j+1][0] - p)
        return f[n][k+1][0]
    
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        f = [[-inf] * 2 for _ in range(k+2)]
        for j in range(k+2):
            f[j][0] = 0
        for p in prices:
            for j in range(k+1):
                f[j+1][0], f[j+1][1] = max(f[j+1][0], f[j][1] + p), max(f[j+1][1], f[j+1][0] - p)
        return f[k+1][0]
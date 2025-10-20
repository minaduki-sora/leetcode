from typing import List
import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # directions = [[0]*n for _ in range(m)]
        sums = [[0]*n for _ in range(m)]
        cnt = 0
        for i in range(n-1, -1, -1):
            cnt += grid[-1][i]
            sums[-1][i] = cnt
            # directions[-1, i] = 1 # right
        cnt = 0
        for i in range(m-1, -1, -1):
            cnt += grid[i][ -1]
            sums[i][-1] = cnt
            # directions[i, -1] = 2 # down
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if sums[i+1][j] < sums[i][j+1]:
                    sums[i][j] = grid[i][j] + sums[i+1][j]
                    # directions[i,j] = 2
                else:
                    sums[i][j] = grid[i][j] + sums[i][j+1]
                    # directions[i,j] = 1
        return sums[0][0]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [40001]*(len(grid[0])+1)
        dp[1] = 0
        for row in grid:
            for i, x in enumerate(row):
                dp[i+1] = min(dp[i], dp[i+1]) + x
        return dp[-1]
        

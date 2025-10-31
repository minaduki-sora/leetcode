import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [10000] * (n+1)
        for i in range(1, math.isqrt(n)+1):
            dp[i*i] = 1
        for i in range(1,n+1):
            if dp[i] != 1:
                for j in range(1,math.isqrt(i)+1):
                    dp[i] = min(dp[i], 1 + dp[i-j*j])
        return dp[n]
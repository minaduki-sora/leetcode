class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[i for i in range(m+1)]] + [[i+1] + [1000] * n for i in range(m)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j], # delete word1[i-1]
                        dp[i-1][j-1], # modify word1[i-1] to word2[j-1]
                        dp[i][j-1] # insert word[j-1] to word1[-1]
                    ) + 1
        return dp[m][n]
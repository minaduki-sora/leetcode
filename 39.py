from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        way = [[[]] * (target+1) for _ in range(n+1)]
        way[0][0] = [[]]
        for i in range(1, n+1):
            for j in range(0, target+1):
                if j >= candidates[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-candidates[i-1]]
                    way[i][j] = [x for x in way[i-1][j]] + [x + [candidates[i-1]] for x in way[i][j-candidates[i-1]]]
                else:
                    dp[i][j] = dp[i-1][j]
                    way[i][j] = [x for x in way[i-1][j]]
        return way[-1][-1]

t = Solution()
t.combinationSum([2,3,6,7], 7)
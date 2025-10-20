from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        wordDict = sorted(wordDict, key=lambda x: len(x))
        for i in range(1, n+1):
            flag = False
            for w in wordDict:
                if len(w) > i or flag:
                    break
                else:
                    flag = dp[i-len(w)] and (w == s[i-len(w):i])
            dp[i] = flag
        return dp[-1]

sol = Solution()
sol.wordBreak("leetcode", ["leet","code"])
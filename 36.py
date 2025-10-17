class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sl = len(s)
        dp = [[False]*sl for _ in range(sl)]
        ml = 0
        for vl in range(2, sl+1, 2):
            for left in range(sl):
                if left + vl > sl:
                    break
                if vl == 2 and s[left] == '(' and s[left+1] == ')':
                    dp[left][left+1] = True
                    if ml < 2:
                        ml = 2
                else:
                    if dp[left+1][left+vl-2] and s[left] == '(' and s[left+vl-1] == ')':
                        dp[left][left+vl-1] = True
                        if ml < vl:
                            ml = vl
                    else:
                        for mid in range(left+1, left+vl-1, 2):
                            dp[left][left+vl-1] = dp[left][mid] and dp[mid+1][left+vl-1]
                            if dp[left][left+vl-1]:
                                if ml < vl:
                                    ml = vl
                                break
        return ml
    
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        maxlen = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i > 2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1]-1] == '(':
                    dp[i] = (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 > 0 else 0) + 2 + dp[i-1]
            maxlen = max(maxlen, dp[i])
        return maxlen

# sol = Solution()
# sol.longestValidParentheses("(()())")
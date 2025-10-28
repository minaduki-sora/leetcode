from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = [""] * (2 * n)
        def dfs(i: int, j: int):
            nonlocal ans, temp
            if 2 * n - i < j:
                return
            if i == 2 * n:
                ans.append("".join(temp))
                return
            temp[i] = "("
            dfs(i+1, j+1)
            if j > 0:
                temp[i] = ")"
                dfs(i+1, j-1)
        dfs(0, 0)
        return ans

t = Solution()
t.generateParenthesis(1)
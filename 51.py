from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        m = [["."] * n for _ in range(n)]
        ans = []

        def conflict(x: int, y: int) -> bool:
            bias = y - x
            for i in range(max(0, -bias), min(n, n-bias)):
                if m[i][i+bias] == 'Q':
                    return True
            
            bias = x + y
            for i in range(max(0, bias-n+1), min(n, bias+1)):
                if m[i][bias-i] == 'Q':
                    return True
            return False
        
        vis = [False] * n
        def dfs(i: int):
            if i == n:
                ans.append(["".join(x) for x in m])
                return
            for j in range(n):
                if vis[j] or conflict(i, j):
                    continue
                vis[j] = True
                m[i][j] = 'Q'
                dfs(i+1)
                vis[j] = False
                m[i][j] = '.'
        dfs(0)
        return ans
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        m = [["."] * n for _ in range(n)]
        diag1 = [False] * (2*n-1)
        diag2 = [False] * (2*n-1)
        vis = [False] * n
        ans = []
        def dfs(i: int):
            if i == n:
                ans.append(["".join(x) for x in m])
                return
            for j in range(n):
                if vis[j] or diag1[i+j] or diag2[i-j]:
                    continue
                vis[j] = diag1[i+j] = diag2[i-j] = True
                m[i][j] = 'Q'
                dfs(i+1)
                vis[j] = diag1[i+j] = diag2[i-j] = False
                m[i][j] = '.'
        dfs(0)
        return ans
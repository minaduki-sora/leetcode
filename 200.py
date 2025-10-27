from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        def dfs(x: int, y: int):
            nonlocal m, n
            if x < 0 or x > m - 1 or y < 0 or y > n - 1:
                return
            if grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt

t = Solution()
t.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
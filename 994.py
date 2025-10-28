from typing import List
import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nxt = copy.deepcopy(grid)
        m = len(grid)
        n = len(grid[0])
        
        def rot(i: int, j: int):
            nonlocal m, n
            flag = False
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = i + a
                y = j + b
                if 0 <= x <= m - 1 and 0 <= y <= n - 1 and nxt[x][y] == 1:
                    nxt[x][y] = 2
                    flag = True
            return flag
        t = 0
        cnt = 0
        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                elif grid[i][j] == 2:
                    flag = rot(i, j) or flag
        while flag:
            t += 1
            cnt = 0
            grid = copy.deepcopy(nxt)
            flag = False
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        cnt += 1
                    elif grid[i][j] == 2:
                        flag = rot(i, j) or flag
        return t if cnt == 0 else -1

so = Solution()
so.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
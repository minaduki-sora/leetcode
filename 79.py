from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):  # 优化一
            return False
        if cnt[word[-1]] < cnt[word[0]]:  # 优化二
            word = word[::-1]
        m = len(board)
        n = len(board[0])
        visit = [[False]*n for _ in range(m)]

        direction = (1, 0), (0, 1), (-1, 0), (0, -1)
        def dfs(i: int, j: int, k: int):
            if i < 0 or i >= m or j < 0 or j >= n or visit[i][j]:
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visit[i][j] = True
            for d in direction:
                if dfs(i + d[0], j + d[1], k + 1):
                    return True
            visit[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

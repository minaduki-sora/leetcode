from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)

        def dfs(i, start):
            if i == n:
                ans.append(path.copy())
                return
            
            if i < n - 1:
                dfs(i + 1, start)
            
            t = s[start:i+1]
            if t == t[::-1]:
                path.append(t)
                dfs(i+1, i+1)
                path.pop()
        
        dfs(0, 0)
        return ans

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)

        def dfs(i: int):
            if i == n:
                ans.append(path.copy())
                return
            
            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans

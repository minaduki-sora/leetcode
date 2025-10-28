from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = defaultdict(list)
        n = numCourses
        visited = [0] * n
        for a, b in prerequisites:
            maps[a].append(b)
        def dfs(i: int):
            if visited[i] == 1:
                return True
            elif visited[i] == 2:
                return False
            visited[i] = 1
            for x in maps[i]:
                if dfs(x):
                    return True
            visited[i] = 2
            return False
        for i in range(n):
            if dfs(i):
                return False
        return True
            

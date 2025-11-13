from typing import List
from collections import defaultdict, OrderedDict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        ans = []
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)

        while stack:
            p = stack.pop()
            ans.append(p)
            for x in adj[p]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    stack.append(x)
            
        return ans if len(ans) == numCourses else []


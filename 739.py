from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
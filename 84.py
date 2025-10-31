from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights= [-1] + heights
        stack = [0]
        for i, x in enumerate(heights[1:]):
            last = stack[-1]
            while len(stack) > 1 and heights[stack[-1]] >= x:
                j = stack.pop()
                ans = max(ans, (last - stack[-1]) * heights[j])
            stack.append(i+1)
        
        last = stack[-1]
        while len(stack) > 1:
            j = stack.pop()
            ans = max(ans, (last - stack[-1]) * heights[j])
        
        return ans
        
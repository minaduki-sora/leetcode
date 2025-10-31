from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        prev = 0
        d = 0
        while d < n - 1:
            np = d + 1
            for i in range(prev, d+1):
                d = max(d, i+nums[i])
            prev = np
            cnt += 1
        return cnt
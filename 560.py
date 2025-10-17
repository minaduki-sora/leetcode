from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = dict()
        s[0] = 1
        cnt = 0
        sums = 0
        for i in range(n):
            sums += nums[i]
            val = sums - k
            x = s.get(val)
            if x:
                cnt += x
            if s.get(sums):
                s[sums] += 1
            else:
                s[sums] = 1
        return cnt
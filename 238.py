from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rac = [0] * n
        
        t = 1
        for i in reversed(range(n)):
            rac[i] = t
            t *= nums[i]
        
        ans = []
        t = 1
        for i in range(n):
            ans.append(t * rac[i])
            t *= nums[i]
        return ans
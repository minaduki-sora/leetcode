from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                continue
            if nums[i] > n:
                nums[i] = -1
                continue
            if nums[i] == i + 1:
                continue
            t = nums[i]
            nums[i] = -1
            while t <= n and t > 0 and nums[t-1] != t:
                p = nums[t-1]
                nums[t-1] = t
                t = p
        for i, x in enumerate(nums):
            if x > n and x <= 0:
                return i + 1
        return n + 1
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1

t = Solution()
t.firstMissingPositive([2,1])
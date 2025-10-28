from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        def dfs(i: int):
            nonlocal ans, temp
            if i == len(nums):
                ans.append(temp.copy())
                return
            dfs(i+1)
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
        dfs(0)
        return ans
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1 << len(nums)):
            subset = [x for j, x in enumerate(nums) if i >> j & 1]
            ans.append(subset)
        return ans
from typing import List, Optional

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp = []
        ans = []
        def dfs(nums: Optional[List[int]]):
            nonlocal ans, temp
            if not nums:
                ans.append(temp.copy())
                return
            for i, x in enumerate(nums):
                temp.append(x)
                dfs(nums[:i] + nums[i+1:])
                temp.pop()
        dfs(nums)
        return ans

t = Solution()
t.permute([1,2,3])
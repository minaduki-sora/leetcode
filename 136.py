from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = [0, 0]
        for x in nums:
            if ans[0] == x:
                ans[1] += 1
            else:
                if ans[1] > 1:
                    ans[1] -= 1
                else:
                    ans[0] = x
                    ans[1] = 1
        return ans[0]
                